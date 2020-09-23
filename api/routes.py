from typing import Tuple

from marshmallow_dataclass import class_schema
from marshmallow import Schema
from pathlib import Path

from numpy import loadtxt, savetxt

from api.blueprints import canvas_api
from api.schemas import RectangleSchema, CanvasSchema, FillOperationSchema
from app import canvas

from flask import Response, request, make_response
from flask_api import status


CANVAS_FILE_PATH: Path = Path(__file__).parent / 'canvas/canvas.csv'


@canvas_api.before_app_first_request
def load_existing_canvas() -> None:
    """
    Load an existing canvas if this is not the first time the application is launched.
    """
    if not CANVAS_FILE_PATH.exists():
        return

    canvas.canvas = loadtxt(
        str(CANVAS_FILE_PATH),
        dtype='U',
        delimiter=','
    )


@canvas_api.after_app_request
def save_canvas_after_request(response: Response) -> Response:
    """
    Save the Canvas object into a CSV file after request to recover it
    on the next application launch.
    """
    savetxt(
        str(CANVAS_FILE_PATH),
        canvas.canvas,
        header='This is a CSV representation of the latest Canvas.',
        fmt='%s',
        delimiter=','
    )

    return response


@canvas_api.route(
    rule='/api/v1/canvas/paint',
    methods=['PUT']
)
def paint_rectangle(**kwargs) -> Tuple[Response, int]:
    """
    Paint a rectangle with the specified parameters on a preexisting canvas.
    """
    json_payload = request.json

    rect_schema: RectangleSchema = RectangleSchema()
    canvas_schema: Schema = class_schema(CanvasSchema)()

    rectangle: dict = rect_schema.load(json_payload)

    canvas.paint_rectangle(
        x=rectangle['x'],
        y=rectangle['y'],
        width=rectangle['width'],
        height=rectangle['height'],
        fill_symbol=rectangle['fill_symbol'],
        outline_symbol=rectangle['outline_symbol']
    )

    canvas.crop_canvas()
    canvas.print_canvas()   # Print the canvas in the console for each call

    json_canvas: dict = canvas_schema.dump(canvas)
    data: dict = {
        'data': json_canvas['canvas']['data'],
        'errors': None
    }

    response: Tuple[Response, int] = make_response(data, status.HTTP_200_OK)

    return response


@canvas_api.route(
    rule='/api/v1/canvas/fill',
    methods=['PUT']
)
def fill_area(**kwargs) -> Tuple[Response, int]:
    """
    Flood fill the points on the canvas, starting from the specified coordinate.
    """
    json_payload = request.json

    fill_schema: FillOperationSchema = FillOperationSchema()
    canvas_schema: Schema = class_schema(CanvasSchema)()

    fill: dict = fill_schema.load(json_payload)

    canvas.fill_area(
        x=fill['x'],
        y=fill['y'],
        fill_symbol=fill['fill_symbol']
    )

    canvas.print_canvas()   # Print the canvas in the console for each call

    json_canvas: dict = canvas_schema.dump(canvas)
    data: dict = {
        'data': json_canvas['canvas']['data'],
        'errors': None
    }

    response: Tuple[Response, int] = make_response(data, status.HTTP_200_OK)

    return response
