from api.canvas.canvas import Canvas
from api.tests.helpers import load_fixture, Rectangle, Fill, CanvasParams

from pathlib import Path
import pytest
import numpy as np


fixture_path_1 = Path(__file__).parent / 'fixtures/expected_canvas_1.csv'
fixture_path_2 = Path(__file__).parent / 'fixtures/expected_canvas_2.csv'
fixture_path_3 = Path(__file__).parent / 'fixtures/expected_canvas_3.csv'


expected_fixture_1: np.array = load_fixture(fixture_path_1)
expected_fixture_2: np.array = load_fixture(fixture_path_2)
expected_fixture_3: np.array = load_fixture(fixture_path_3)


fixture_1 = (
    [
        Rectangle(3, 2, 5, 3, 'x', '@'),
        Rectangle(10, 3, 14, 6, 'O', 'X')
    ],
    None,
    CanvasParams(10, 25, ' '),
    expected_fixture_1
)

fixture_2 = (
    [
        Rectangle(14, 0, 7, 6, '.', None),
        Rectangle(0, 3, 8, 4, None, 'O'),
        Rectangle(5, 5, 5, 3, 'X', 'X')
    ],
    None,
    CanvasParams(9, 22, ' '),
    expected_fixture_2
)

fixture_3 = (
    [
        Rectangle(14, 0, 7, 6, '.', None),
        Rectangle(0, 3, 8, 4, None, 'O'),
        Rectangle(5, 5, 5, 3, 'X', 'X')
    ],
    Fill(0, 0, '-'),
    CanvasParams(9, 22, ' '),
    expected_fixture_3
)


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
        is_success, _ = canvas.paint_rectangle(
            x=params.x,
            y=params.y,
            width=params.width,
            height=params.height,
            fill_symbol=params.fill_symbol,
            outline_symbol=params.outline_symbol
        )
        assert is_success == True

    if fill_args:
        is_success, _ = canvas.fill_area(*fill_args)
        assert is_success == True

    assert np.array_equal(canvas.canvas, expected)
