import pytest
import numpy as np

from api.canvas.canvas import Canvas
from tests.params import fixture_1, fixture_2, fixture_3


@pytest.mark.parametrize(
    'paint_rectangle_args, fill_args, canvas_args, expected',
    [
        fixture_1,
        fixture_2,
        fixture_3
    ]
)
def test_canvas(paint_rectangle_args, fill_args, canvas_args, expected):
    """
    Test given fixtures to make sure that methods in Canvas class behave as expected.
    """
    canvas: Canvas = Canvas(
        *canvas_args
    )

    for params in paint_rectangle_args:
        is_success, errors, _ = canvas.paint_rectangle(
            x=params.x,
            y=params.y,
            width=params.width,
            height=params.height,
            fill_symbol=params.fill_symbol,
            outline_symbol=params.outline_symbol
        )
        assert is_success == True, errors

    if fill_args:
        is_success, errors, _ = canvas.fill_area(*fill_args)
        assert is_success == True, errors

    assert np.array_equal(canvas.canvas, expected)
