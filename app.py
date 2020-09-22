from api import CanvasAPI
from api.canvas.canvas import Canvas

from flask import Response, Flask, make_response
from flask_api import status
from typing import Tuple
from werkzeug.exceptions import HTTPException


app: Flask = CanvasAPI.create_app()
canvas: Canvas = Canvas(rows=100, cols=100, fill_symbol=' ')


@app.errorhandler(Exception)
def handle_uncaught_exception(error: Exception) -> Tuple[Response, int]:
    """
    Handle a generic unhandled exception that might occur within the request context.

    :param error: an exception object
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_string = f'Uncaught Exception: {str(error)}'

    if isinstance(error, HTTPException):
        status_code = error.code

    data = {
        'data': None,
        'errors': error_string
    }
    response = make_response(
        data, status_code
    )

    return response


if __name__ == '__main__':
    """
    Start the Flask server.
    """
    app.run()
