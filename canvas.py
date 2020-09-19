from typing import Tuple


class Canvas:
    """ A class representing an ASCII canvas. """
    def __init__(
            self,
            rows: int, cols: int, fill_symbol: str = ' '
    ) -> None:
        """
        Initialize an empty canvas with the specified width and height.

        :param rows:        height of the rectangle
        :param cols:        width of the rectangle
        :param fill_symbol: the initial symbol to fill the canvas with
        """
        self.rows = rows
        self.cols = cols

        self.canvas = [[fill_symbol] * self.cols for _ in range(self.rows)]

    def __calculate_canvas_size(self) -> Tuple[int, int]:
        """
        NOTE: This is a placeholder function for now.
        Calculate the minimum desired size of the canvas based on the drawn rectangles.
        """
        pass

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
        pass

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
        pass

    def print_canvas(self) -> None:
        """
        Print the contents of the current canvas.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.canvas[row][col], end=' ')
            print('\r')


if __name__ == '__main__':
    canvas = Canvas(rows=5, cols=5, fill_symbol='N')
    canvas.print_canvas()
