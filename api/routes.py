import marshmallow_dataclass
from marshmallow import Schema

from api.blueprints import canvas_api
from api.schemas import RectangleSchema, CanvasSchema
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

    rectangle = rect_schema.load(json_payload)

    canvas.paint_rectangle(
        x=rectangle['x'],
        y=rectangle['y'],
        width=rectangle['width'],
        height=rectangle['height'],
        fill_symbol=rectangle['fill_symbol'],
        outline_symbol=rectangle['outline_symbol']
    )

    canvas.crop_canvas()

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
def fill_points(**kwargs) -> Response:
    """
    Flood fill the points on the canvas, starting from the specified coordinate.
    """
    pass
