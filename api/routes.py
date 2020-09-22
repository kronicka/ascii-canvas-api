import marshmallow_dataclass
from marshmallow import Schema

from api.blueprints import canvas_api
from api.schemas import RectangleSchema, CanvasSchema, FillOperationSchema
from app import canvas

from flask import Response, request, make_response
from flask_api import status


@canvas_api.route(
    rule='/api/v1/canvas/paint',
    methods=['PUT']
)
def paint_rectangle(**kwargs) -> Response:
    """
    Paint a rectangle with the specified parameters on a preexisting canvas.
    """
    json_payload = request.json

    rect_schema: RectangleSchema = RectangleSchema()
    canvas_schema: Schema = marshmallow_dataclass.class_schema(CanvasSchema)()

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

    response = make_response(data, status.HTTP_200_OK)

    return response


@canvas_api.route(
    rule='/api/v1/canvas/fill',
    methods=['PUT']
)
def fill_area(**kwargs) -> Response:
    """
    Flood fill the points on the canvas, starting from the specified coordinate.
    """
    json_payload = request.json

    fill_schema: FillOperationSchema = FillOperationSchema()
    canvas_schema: Schema = marshmallow_dataclass.class_schema(CanvasSchema)()

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

    response = make_response(data, status.HTTP_200_OK)

    return response
