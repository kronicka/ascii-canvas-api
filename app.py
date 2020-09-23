from api import CanvasAPI
from api.canvas.canvas import Canvas

from flask import Response, Flask, make_response
from flask_api import status
from typing import Tuple
from werkzeug.exceptions import HTTPException


app: Flask = CanvasAPI.create_app()
canvas: Canvas = Canvas(rows=35, cols=35, fill_symbol=' ')


@app.errorhandler(Exception)
def handle_uncaught_exception(error: Exception) -> Tuple[Response, int]:
    """
    Handle a generic unhandled exception that might occur within the request context.

    :param error: an exception object
    """
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_string: str = f'Uncaught Exception: {str(error)}'

    if isinstance(error, HTTPException):
        status_code = error.code

    data: dict = {
        'data': None,
        'errors': error_string
    }
    response: Tuple[Response, int] = make_response(
        data, status_code
    )

    return response


if __name__ == '__main__':
    """
    Start the Flask server.
    """
    app.run()
