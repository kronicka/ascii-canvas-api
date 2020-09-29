import numpy as np

from flask_api import status
from tests.helpers import load_fixture, Rectangle, Fill, CanvasParams

from pathlib import Path

"""
Parameters for Canvas Unit Tests
"""

fixture_path_1: Path = Path(__file__).parent / 'fixtures/expected_canvas_1.csv'
fixture_path_2: Path = Path(__file__).parent / 'fixtures/expected_canvas_2.csv'
fixture_path_3: Path = Path(__file__).parent / 'fixtures/expected_canvas_3.csv'


expected_fixture_1: np.array = load_fixture(fixture_path_1)
expected_fixture_2: np.array = load_fixture(fixture_path_2)
expected_fixture_3: np.array = load_fixture(fixture_path_3)


fixture_1 = (
    [
        Rectangle(3, 2, 5, 3, 'X', '@'),
        Rectangle(10, 3, 14, 6, 'O', 'X')
    ],
    None,
    CanvasParams(9, 24, ' '),
    expected_fixture_1
)

fixture_2 = (
    [
        Rectangle(14, 0, 7, 6, '.', None),
        Rectangle(0, 3, 8, 4, None, 'O'),
        Rectangle(5, 5, 5, 3, 'X', 'X')
    ],
    None,
    CanvasParams(8, 21, ' '),
    expected_fixture_2
)

fixture_3 = (
    [
        Rectangle(14, 0, 7, 6, '.', None),
        Rectangle(0, 3, 8, 4, None, 'O'),
        Rectangle(5, 5, 5, 3, 'X', 'X')
    ],
    Fill(0, 0, '-'),
    CanvasParams(8, 21, ' '),
    expected_fixture_3
)


"""
Parameters for Canvas API Tests
"""

# Paint Rectangle Test Payloads
paint_rectangle_success_payload_1 = (
    {
        "x": 10,
        "y": 6,
        "width": 5,
        "height": 5,
        "fill_symbol": "O",
        "outline_symbol": "*"
    },
    status.HTTP_200_OK
)

paint_rectangle_success_payload_2 = (
    {
        "x": 2,
        "y": 14,
        "width": 7,
        "height": 5,
        "fill_symbol": "?"
    },
    status.HTTP_200_OK
)

paint_rectangle_success_payload_3 = (
    {
        "x": 0,
        "y": 8,
        "width": 10,
        "height": 8,
        "outline_symbol": "!"
    },
    status.HTTP_200_OK
)

paint_rectangle_fail_payload_1 = (
    {
        "x": 3,
        "y": 1,
        "width": 3,
        "height": 4
    },
    status.HTTP_400_BAD_REQUEST
)

paint_rectangle_fail_payload_2 = (
    {
        "x": 3,
        "y": 1,
        "height": 4,
        "outline_symbol": "X"
    },
    status.HTTP_400_BAD_REQUEST
)


paint_rectangle_fail_payload_3 = (
    {
        "x": -3,
        "y": 1,
        "height": 4,
        "outline_symbol": "X",
        "fill_symbol": "."
    },
    status.HTTP_400_BAD_REQUEST
)


# Fill Operation Test Payloads
fill_success_payload_1 = (
    {
        "x": 0,
        "y": 0,
        "fill_symbol": "-"
    },
    status.HTTP_200_OK
)

fill_success_payload_2 = (
    {
        "x": 5,
        "y": 6,
        "fill_symbol": "O"
    },
    status.HTTP_200_OK
)

fill_fail_payload_1 = (
    {
        "x": -1,
        "y": 6,
        "fill_symbol": "K"
    },
    status.HTTP_400_BAD_REQUEST
)

fill_fail_payload_2 = (
    {
        "x": 3,
        "y": 3
    },
    status.HTTP_400_BAD_REQUEST
)
