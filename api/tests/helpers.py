from typing import NamedTuple, Union
import numpy as np
from pathlib import Path

"""
Named Tuples representing the expected function arguments.
"""


class Rectangle(NamedTuple):
    x: int
    y: int
    width: int
    height: int
    fill_symbol: Union[str, None]
    outline_symbol: Union[str, None]


class Fill(NamedTuple):
    x: int
    y: int
    fill_symbol: str


class CanvasParams(NamedTuple):
    rows: int
    cols: int
    fill_symbol: str


def load_fixture(file_path: Path) -> np.array:
    """
    Load the appropriate Canvas fixture for testing.

    :param file_path: the location of the fixture
    :return:          a numpy array loaded from a CVS file
    """
    if not file_path.exists():
        return

    fixture = None

    try:
        fixture = np.loadtxt(
            str(file_path),
            dtype='<U1',
            delimiter='¬',
            comments='¤'
        )
    except ValueError as e:
        print(
            f'Something went wrong loading from the file.'
            f' Details: {e}'
        )

    return fixture
