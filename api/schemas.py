from marshmallow.validate import Length

from factory import ma
from marshmallow import fields

import marshmallow_dataclass
from marshmallow_numpy import NumpyArray


@marshmallow_dataclass.dataclass
class CanvasSchema:
    """
    A Marshmallow schema to serialize the Canvas object as JSON.
    """
    canvas: NumpyArray


class RectangleSchema(ma.Schema):
    """
    A Marshmallow schema to validate structural correctness of the passed in Rectangle properties.
    """
    x = fields.Int()
    y = fields.Int()
    width = fields.Int()
    height = fields.Int()

    fill_symbol = fields.String(
        validate=Length(min=1, max=1),
        allow_none=True
    )
    outline_symbol = fields.String(
        validate=Length(min=1, max=1),
        allow_none=True
    )


class FillOperationSchema(ma.Schema):
    """
    A Marshmallow schema to validate structural correctness of the passed in Fill operation properties.
    """
    pass