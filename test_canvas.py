from canvas import Canvas


def test_fixture_1():
    """
    Test fixture 1 separated into a function.

    Input:
    - Rectangle at [3,2] with width: 5, height: 3, outline character: `@`, fill character: `X`
    - Rectangle at [10, 3] with width: 14, height: 6, outline character: `X`, fill character: `O`

    Expected output:


       @@@@@
       @XXX@  XXXXXXXXXXXXXX
       @@@@@  XOOOOOOOOOOOOX
              XOOOOOOOOOOOOX
              XOOOOOOOOOOOOX
              XOOOOOOOOOOOOX
              XXXXXXXXXXXXXX

    """
    canvas: Canvas = Canvas(rows=100, cols=100, fill_symbol=' ')

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

    print('\nThis is Test Fixture 1: ')
    canvas.print_canvas()


def test_fixture_2():
    """
    Test fixture 2 separated into a function.

    Input:
    - Rectangle at `[14, 0]` with width `7`, height `6`, outline character: none, fill: `.`
    - Rectangle at `[0, 3]` with width `8`, height `4`, outline character: `O`, fill: `none`
    - Rectangle at `[5, 5]` with width `5`, height `3`, outline character: `X`, fill: `X`

    Expected output:
                  .......
                  .......
                  .......
    OOOOOOOO      .......
    O      O      .......
    O    XXXXX    .......
    OOOOOXXXXX
         XXXXX

    """
    canvas: Canvas = Canvas(rows=500, cols=500, fill_symbol=' ')

    rx_1, ry_1, rwidth_1, rheight_1, fill_symbol_1, outline_symbol_1 = 14, 0, 7, 6, '.', None
    canvas.paint_rectangle(
        x=rx_1,
        y=ry_1,
        width=rwidth_1,
        height=rheight_1,
        fill_symbol=fill_symbol_1,
        outline_symbol=outline_symbol_1
    )

    rx_2, ry_2, rwidth_2, rheight_2, fill_symbol_2, outline_symbol_2 = 0, 3, 8, 4, None, 'O'
    canvas.paint_rectangle(
        x=rx_2,
        y=ry_2,
        width=rwidth_2,
        height=rheight_2,
        fill_symbol=fill_symbol_2,
        outline_symbol=outline_symbol_2
    )

    rx_3, ry_3, rwidth_3, rheight_3, fill_symbol_3, outline_symbol_3 = 5, 5, 5, 3, 'X', 'X'
    canvas.paint_rectangle(
        x=rx_3,
        y=ry_3,
        width=rwidth_3,
        height=rheight_3,
        fill_symbol=fill_symbol_3,
        outline_symbol=outline_symbol_3
    )

    print('\nThis is Test Fixture 2: ')
    canvas.print_canvas()


def test_fixture_3():
    """
    Test fixture 3 separated into a function.

    TODO: Fix the canvas cropping according to this test fixture.

    Input:
    - Rectangle at `[14, 0]` with width `7`, height `6`, outline character: none, fill: `.`
    - Rectangle at `[0, 3]` with width `8`, height `4`, outline character: `O`, fill: `none`
    - Rectangle at `[5, 5]` with width `5`, height `3`, outline character: `X`, fill: `X`
    - Flood fill at `[0, 0]` with fill character `-` (canvas presented in 32x12 size)

    Expected output:
    --------------.......
    --------------.......
    --------------.......
    OOOOOOOO------.......
    O      O------.......
    O    XXXXX----.......
    OOOOOXXXXX-----------
         XXXXX-----------

    """
    canvas: Canvas = Canvas(rows=500, cols=500, fill_symbol=' ')

    rx_1, ry_1, rwidth_1, rheight_1, fill_symbol_1, outline_symbol_1 = 14, 0, 7, 6, '.', None
    canvas.paint_rectangle(
        x=rx_1,
        y=ry_1,
        width=rwidth_1,
        height=rheight_1,
        fill_symbol=fill_symbol_1,
        outline_symbol=outline_symbol_1
    )

    rx_2, ry_2, rwidth_2, rheight_2, fill_symbol_2, outline_symbol_2 = 0, 3, 8, 4, None, 'O'
    canvas.paint_rectangle(
        x=rx_2,
        y=ry_2,
        width=rwidth_2,
        height=rheight_2,
        fill_symbol=fill_symbol_2,
        outline_symbol=outline_symbol_2
    )

    rx_3, ry_3, rwidth_3, rheight_3, fill_symbol_3, outline_symbol_3 = 5, 5, 5, 3, 'X', 'X'
    canvas.paint_rectangle(
        x=rx_3,
        y=ry_3,
        width=rwidth_3,
        height=rheight_3,
        fill_symbol=fill_symbol_3,
        outline_symbol=outline_symbol_3
    )

    canvas.fill_rectangle(0, 0, '-')

    print('\nThis is Test Fixture 3: ')
    canvas.print_canvas()


if __name__ == '__main__':
    """
    Run test fixtures in the console.
    """
    test_fixture_1()
    test_fixture_2()
    test_fixture_3()
