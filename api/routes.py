import json
from typing import Tuple

from marshmallow_dataclass import class_schema
from marshmallow import Schema
from pathlib import Path

from numpy import loadtxt, savetxt

from api.blueprints import canvas_api
from api.helpers.sse_events import event_stream
from api.schemas import RectangleSchema, CanvasSchema, FillOperationSchema
from app import canvas, strict_redis

from flask import Response, request, make_response, render_template
from flask_api import status


CANVAS_FILE_PATH: Path = Path(__file__).parent / 'canvas/canvas.csv'


@canvas_api.before_app_first_request
def load_existing_canvas() -> None:
    """
    Load an existing canvas if this is not the first time the application is launched.

    NOTE:   Delimiters and comments are non-ASCII characters, so that they are not confused
          with symbols on the Canvas.
    """
    if not CANVAS_FILE_PATH.exists():
        return

    try:
        canvas.canvas = loadtxt(
            str(CANVAS_FILE_PATH),
            dtype='<U1',
            delimiter='¬',
            comments='¤'
        )
    except ValueError as e:
        print(
            f'Something went wrong loading from the file.'
            f' Details: {e}'
        )


@canvas_api.after_app_request
def save_canvas_after_request(response: Response) -> Response:
    """
    Save the Canvas object into a CSV file after request to recover it
    on the next application launch.

    NOTE:   Delimiters and comments are non-ASCII characters, so that they are not confused
          with symbols on the Canvas.
    """
    savetxt(
        str(CANVAS_FILE_PATH),
        canvas.canvas,
        header='This is a CSV representation of the latest Canvas.',
        fmt='%s',
        delimiter='¬',
        comments='¤'
    )

    return response


@canvas_api.route(rule='/stream')
def stream_changes() -> Response:
    """
    Stream any Canvas modifications from the server side directly to the JS template.
    """
    return Response(
        event_stream(),
        mimetype='text/event-stream'
    )


@canvas_api.route(
    rule='/',
    methods=['GET']
)
def get_index_page() -> Tuple[Response, int]:
    """
    Render the Main Page, containing the canvas.

    NOTE:   `first_canvas` field is only gonna be rendered once per canvas page reload.
          It is needed for the initial render, not caused by messages being published
          onto the stream.
            A cached version of `first_canvas` should be used, if the canvas hasn't changed
          before the reload.
    """
    return render_template(
        'index.html', first_canvas=canvas.canvas
    )


@canvas_api.route(
    rule='/api/v1/canvas/paint',
    methods=['PUT']
)
def paint_rectangle() -> Tuple[Response, int]:
    """
    Paint a rectangle with the specified parameters on a preexisting canvas.
    """
    json_payload = request.json
    response_data: dict = {
        'data': None,
        'errors': None
    }

    rect_schema: RectangleSchema = RectangleSchema()
    canvas_schema: Schema = class_schema(CanvasSchema)()

    rectangle: dict = rect_schema.load(json_payload)

    is_success, errors = canvas.paint_rectangle(
        x=rectangle['x'],
        y=rectangle['y'],
        width=rectangle['width'],
        height=rectangle['height'],
        fill_symbol=rectangle['fill_symbol'],
        outline_symbol=rectangle['outline_symbol']
    )

    if not is_success:
        response_data['errors'] = errors
        return make_response(
            response_data, status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Return a serialized JSON version of the canvas with the REST response
    json_canvas: dict = canvas_schema.dump(canvas)
    response_data['data'] = json_canvas['canvas']['data']

    strict_redis.publish(
        channel='canvas_changes',
        message=json.dumps(json_canvas['canvas'])
    )
    response: Tuple[Response, int] = make_response(
        response_data, status.HTTP_200_OK
    )

    return response


@canvas_api.route(
    rule='/api/v1/canvas/fill',
    methods=['PUT']
)
def fill_area() -> Tuple[Response, int]:
    """
    Flood fill the points on the canvas, starting from the specified coordinate.
    """
    json_payload = request.json
    response_data: dict = {
        'data': None,
        'errors': None
    }

    fill_schema: FillOperationSchema = FillOperationSchema()
    canvas_schema: Schema = class_schema(CanvasSchema)()

    fill: dict = fill_schema.load(json_payload)

    is_success, errors = canvas.fill_area(
        x=fill['x'],
        y=fill['y'],
        fill_symbol=fill['fill_symbol']
    )

    if not is_success:
        response_data['errors'] = errors
        return make_response(
            response_data, status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Return a serialized JSON version of the canvas with the REST response
    json_canvas: dict = canvas_schema.dump(canvas)
    response_data['data'] = json_canvas['canvas']['data']

    strict_redis.publish(
        channel='canvas_changes',
        message=json.dumps(json_canvas['canvas'])
    )
    response: Tuple[Response, int] = make_response(response_data, status.HTTP_200_OK)

    return response
