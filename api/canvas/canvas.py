from collections import deque
from typing import Tuple, Optional
import numpy as np
from flask_api import status


class Canvas:
    """ A class representing an ASCII canvas. """
    def __init__(
            self,
            rows: int = 100, cols: int = 100, fill_symbol: str = ' '
    ) -> None:
        """
        Initialize an empty canvas with the specified height and width.

        :param rows:        height of the rectangle
        :param cols:        width of the rectangle
        :param fill_symbol: the initial symbol to fill the canvas with
        """
        self.__rows: int = rows
        self.__cols: int = cols

        self.__painted_lowest_border: int = 0
        self.__painted_rightmost_border: int = 0

        self.canvas: np.array = np.array(
            [[fill_symbol] * self.__cols for _ in range(self.__rows)]
        )

    def __check_rectangle_in_range(
            self,
            first_row: int, last_row: int,
            first_col: int, last_col: int
    ) -> bool:
        """
        Check if the specified rectangle can be placed on the canvas of the current size.

        :param first_row: index of the upper border of the rectangle
        :param last_row:  index of the lower border of the rectangle
        :param first_col: index of the rightmost border of the rectangle
        :param last_col:  index of the leftmost border of the rectangle

        :return:          true if the rectangle can be added to the current canvas, false if not
        """
        return (0 <= first_row and last_row < self.__rows) and (0 <= first_col and last_col < self.__cols)

    def __crop_canvas(self) -> None:
        """
        Crop canvas just enough to fit in currently painted rectangles.
        """
        if not self.__painted_lowest_border and not self.__painted_rightmost_border:
            # Return if no rectangles have previously been placed on the canvas
            return

        self.__rows = self.__painted_lowest_border
        self.__cols = self.__painted_rightmost_border
        self.canvas = self.canvas[:self.__rows, :self.__cols]

    def __fill_vertical_borders(
        self,
        start: int, end: int,
        leftmost_border: int, rightmost_border: int, fill_symbol: str
    ) -> None:
        """
        Fill the leftmost and the rightmost border of a rectangle with an outline.

        :param start:            y-position of each first element in the column
        :param end:              y-position of each last element in the column
        :param leftmost_border:  x-position of the first column to fill
        :param rightmost_border: x-position of the last column to fill
        :param fill_symbol:      symbol to fill the column with
        """
        for char in range(start, end + 1):
            self.canvas[char][leftmost_border] = fill_symbol
            self.canvas[char][rightmost_border] = fill_symbol

    def __fill_horizontal_borders(
            self,
            start: int, end: int,
            upper_border: int, lower_border: int, fill_symbol: str
    ) -> None:
        """
        Fill the upper and the lower border of a rectangle with an outline.

        :param start:        start position of the line to fill in
        :param end:          end position of the line to fill in
        :param upper_border: number of the top line to fill in
        :param lower_border: number of the bottom line to fill in
        :param fill_symbol:  symbol to fill the line with
        """
        for char in range(start, end + 1):
            self.canvas[upper_border][char] = fill_symbol
            self.canvas[lower_border][char] = fill_symbol

    def paint_rectangle(
        self,
        x: int, y: int, width: int, height: int,
        fill_symbol: str = None, outline_symbol: str = None
    ) -> Tuple[bool, Optional[str], int]:
        """
        Paint a rectangle on the canvas.

        :param x:              x-coordinate for the position of the upper left corner of the rectangle
        :param y:              y-coordinate for the position of the upper left corner of the rectangle
        :param width:          width of the rectangle
        :param height:         height of the rectangle
        :param fill_symbol:    the symbol to fill in the rectangle with
        :param outline_symbol: the symbol for the outline
        """
        is_success: bool = False
        error_message: Optional[str] = None
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

        first_row: int = y
        last_row: int = height + y - 1
        first_col: int = x
        last_col: int = width + x - 1

        in_range_check = self.__check_rectangle_in_range(
            first_row=first_row,
            last_row=last_row,
            first_col=first_col,
            last_col=last_col
        )

        if not in_range_check:
            error_message = (
                f'This rectangle will not fit on the current canvas. '
                f'Please specify the rectangle within this range: {self.__cols}x{self.__rows}'
            )
            status_code = status.HTTP_400_BAD_REQUEST
            return is_success, error_message, status_code

        if not outline_symbol and not fill_symbol:
            error_message = (
                'No outline or fill symbol has been specified for the rectangle. '
                'Please specify fill_symbol or outline_symbol field.'
            )
            status_code = status.HTTP_400_BAD_REQUEST
            return is_success, error_message, status_code

        try:
            # Keep track of the lowest rightmost border painted to be able to crop the canvas accordingly
            self.__painted_lowest_border = max(self.__painted_lowest_border, last_row)
            self.__painted_rightmost_border = max(self.__painted_rightmost_border, last_col)

            if outline_symbol:
                self.__fill_horizontal_borders(
                    start=first_col,
                    end=last_col,
                    upper_border=first_row,
                    lower_border=last_row,
                    fill_symbol=outline_symbol
                )

                # These are needed to avoid filling the points already covered by adding horizontal borders
                first_row += 1
                last_row -= 1

                self.__fill_vertical_borders(
                    start=first_row,
                    end=last_row,
                    leftmost_border=first_col,
                    rightmost_border=last_col,
                    fill_symbol=outline_symbol
                )

                # These are needed to avoid filling the points already covered by adding vertical borders
                first_col += 1
                last_col -= 1

            if fill_symbol:
                for row in range(first_row, last_row + 1):
                    for col in range(first_col, last_col + 1):
                        self.canvas[row][col] = fill_symbol

            is_success = True
            status_code = status.HTTP_200_OK

        except Exception as e:
            error_message = f'Something went wrong while attempting to paint the rectangle. ' \
                            f'Details: {e}'

        return is_success, error_message, status_code

    def fill_area(
        self,
        x: int, y: int, fill_symbol: str
    ) -> Tuple[bool, Optional[str], int]:
        """
        Fill an entity on the canvas with the specified symbol.

        :param x:           x-coordinate of any point on the entity to fill in
        :param y:           y-coordinate of any point on the entity to fill in
        :param fill_symbol: the symbol to fill the entity with
        """
        is_success: bool = False
        error_message: Optional[str] = None
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

        try:
            if x < 0 or x >= self.__cols or y < 0 or y >= self.__rows:
                error_message = (
                    f'The canvas is {self.__cols}x{self.__rows}. Try passing valid coordinates :-)'
                )
                status_code = status.HTTP_400_BAD_REQUEST
                return is_success, error_message, status_code

            initial_symbol: str = self.canvas[y][x]

            if initial_symbol == fill_symbol:
                is_success = True  # No need to fill if the initial symbol matches the fill symbol.
                status_code = status.HTTP_200_OK
                return is_success, error_message, status_code

            self.canvas[y][x] = fill_symbol
            neighbours: deque = deque()
            neighbours.append((y, x))

            while neighbours:
                row, col = neighbours.popleft()

                up: int = row - 1
                down: int = row + 1
                left: int = col - 1
                right: int = col + 1

                # Push the matching symbols onto the queue to see if they extend the filled area
                if up >= 0 and self.canvas[up][col] == initial_symbol:
                    self.canvas[up][col] = fill_symbol
                    neighbours.append((up, col))

                if down < self.__rows and self.canvas[down][col] == initial_symbol:
                    self.canvas[down][col] = fill_symbol
                    neighbours.append((down, col))

                if left >= 0 and self.canvas[row][left] == initial_symbol:
                    self.canvas[row][left] = fill_symbol
                    neighbours.append((row, left))

                if right < self.__cols and self.canvas[row][right] == initial_symbol:
                    self.canvas[row][right] = fill_symbol
                    neighbours.append((row, right))

            is_success = True
            status_code = status.HTTP_200_OK

        except Exception as e:
            error_message = f'Something went wrong while filling an area. ' \
                            f'Details: {e}'

        return is_success, error_message, status_code
