from typing import Tuple
from collections import deque


class Canvas:
    """ A class representing an ASCII canvas. """
    def __init__(
            self,
            rows: int, cols: int, fill_symbol: str = ' '
    ) -> None:
        """
        Initialize an empty canvas with the specified height and width.

        :param rows:        height of the rectangle
        :param cols:        width of the rectangle
        :param fill_symbol: the initial symbol to fill the canvas with
        """
        self.rows: int = rows
        self.cols: int = cols

        self.canvas: list = [[fill_symbol] * self.cols for _ in range(self.rows)]

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
        return (0 < first_row and last_row < self.rows) and (0 < first_col and last_col < self.cols)

    def __calculate_canvas_size(self) -> Tuple[int, int]:
        """
        NOTE: This is a placeholder function for now.
        Calculate the minimum desired size of the canvas based on the drawn rectangles.
        """
        pass

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
        for char in range(start, end):
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
        for char in range(start, end):
            self.canvas[upper_border][char] = fill_symbol
            self.canvas[lower_border][char] = fill_symbol

    def paint_rectangle(
        self,
        x: int, y: int, width: int, height: int,
        fill_symbol: str = None, outline_symbol: str = None
    ) -> None:
        """
        Paint a rectangle on the canvas.

        :param x:              x-coordinate for the position of the upper left corner of the rectangle
        :param y:              y-coordinate for the position of the upper left corner of the rectangle
        :param width:          width of the rectangle
        :param height:         height of the rectangle
        :param fill_symbol:    the symbol to fill in the rectangle with
        :param outline_symbol: the symbol for the outline
        """
        first_row: int = y
        last_row: int = height + y
        first_col: int = x
        last_col: int = width + x

        in_range_check = self.__check_rectangle_in_range(
            first_row=first_row,
            last_row=last_row,
            first_col=first_col,
            last_col=last_col
        )

        if not in_range_check:
            print(
                f'This rectangle will not fit on the current canvas. '
                f'Please specify the rectangle within this range: {self.rows}x{self.cols}'
            )
            return

        if not outline_symbol and not fill_symbol:
            print(
                'No outline or fill symbol has been specified for the rectangle. '
                'Please specify fill_symbol or outline_symbol field.'
            )
            return

        if outline_symbol:
            self.__fill_horizontal_borders(
                start=first_col,
                end=last_col,
                upper_border=first_row,
                lower_border=last_row - 1,
                fill_symbol=outline_symbol
            )

            # These are needed to avoid filling the points already covered by adding horizontal borders
            first_row += 1
            last_row -= 1

            if not fill_symbol:
                self.__fill_vertical_borders(
                    start=first_row,
                    end=last_row,
                    leftmost_border=first_col,
                    rightmost_border=last_col - 1,
                    fill_symbol=outline_symbol
                )

        if fill_symbol:
            for curr_y in range(first_row, last_row):
                for curr_x in range(first_col, last_col):
                    if outline_symbol and (curr_x == first_col or curr_x == last_col - 1):
                        self.canvas[curr_y][curr_x] = outline_symbol
                    else:
                        self.canvas[curr_y][curr_x] = fill_symbol

    def fill_rectangle(
        self,
        x: int, y: int, fill_symbol: str
    ) -> None:
        """
        Fill an entity on the canvas with the specified symbol.

        :param x:           x-coordinate of any point on the entity to fill in
        :param y:           y-coordinate of any point on the entity to fill in
        :param fill_symbol: the symbol to fill the entity with
        """
        try:
            if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
                print(
                    f'The canvas is {self.rows}x{self.cols}. Try passing valid coordinates :-)'
                )

            initial_symbol: str = self.canvas[y][x]
            neighbours: deque = deque()

            self.canvas[y][x] = fill_symbol
            neighbours.append((y, x))

            while neighbours:
                curr_y, curr_x = neighbours.popleft()

                up: int = curr_y - 1
                down: int = curr_y + 1
                left: int = curr_x - 1
                right: int = curr_x + 1

                if up >= 0 and self.canvas[up][curr_x] == initial_symbol:
                    self.canvas[up][curr_x] = fill_symbol
                    neighbours.append((up, curr_x))

                if down < self.rows and self.canvas[down][curr_x] == initial_symbol:
                    self.canvas[down][curr_x] = fill_symbol
                    neighbours.append((down, curr_x))

                if left >= 0 and self.canvas[curr_y][left] == initial_symbol:
                    self.canvas[curr_y][left] = fill_symbol
                    neighbours.append((curr_y, left))

                if right < self.cols and self.canvas[curr_y][right] == initial_symbol:
                    self.canvas[curr_y][right] = fill_symbol
                    neighbours.append((curr_y, right))

        except Exception as e:
            print(f'Something went wrong: {e}')

    def print_canvas(
            self,
            crop_bottom: int = 0, crop_right: int = 0
    ) -> None:
        """
        Print the contents of the current canvas.

        :param crop_bottom: line to crop the canvas horizontally at
        :param crop_right:  column to crop the canvas vertically at
        """
        rows = self.rows - (self.rows - crop_bottom) or self.rows
        cols = self.cols - (self.cols - crop_right) or self.cols

        for row in range(rows):
            for col in range(cols):
                print(self.canvas[row][col], end=' ')
            print('\r')


if __name__ == '__main__':
    """
    - x=3 y=2 width=5 height=3 fill=`@` outline=None 
    - x=10 y=3 width=14 height=6 fill=`O` outline=`X`

    ```


       @@@@@
       @xxx@  XXXXXXXXXXXXXX
       @@@@@  XOOOOOOOOOOOOX
              XOOOOOOOOOOOOX
              XOOOOOOOOOOOOX
              XOOOOOOOOOOOOX
              XXXXXXXXXXXXXX
    ```
    """

    canvas: Canvas = Canvas(rows=1000, cols=1000, fill_symbol=' ')

    rx_1, ry_1, rwidth_1, rheight_1, fill_symbol_1, outline_symbol_1 = 3, 2, 5, 3, 'x', '@'
    canvas.paint_rectangle(
        x=rx_1,
        y=ry_1,
        width=rwidth_1,
        height=rheight_1,
        fill_symbol=fill_symbol_1,
        outline_symbol=outline_symbol_1
    )

    rx_2, ry_2, rwidth_2, rheight_2, fill_symbol_2, outline_symbol_2 = 10, 3, 9, 6, 'O', 'X'
    canvas.paint_rectangle(
        x=rx_2,
        y=ry_2,
        width=rwidth_2,
        height=rheight_2,
        fill_symbol=fill_symbol_2,
        outline_symbol=outline_symbol_2
    )

    canvas.fill_rectangle(0, 0, '-')
    canvas.fill_rectangle(4, 3, 'M')

    crop_bottom = max(
        ry_1 + rheight_1 + 1,
        ry_2 + rheight_2 + 1
    )
    crop_right = max(
        rx_1 + rwidth_1 + 1,
        rx_2 + rwidth_2 + 1
    )

    canvas.print_canvas(crop_bottom=crop_bottom, crop_right=crop_right)
