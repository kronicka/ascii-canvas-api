from flask import Blueprint
from flask_cors import CORS
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / 'templates'

canvas_api = Blueprint(
    'canvas_api',
    __name__,
    template_folder=TEMPLATE_PATH
)
CORS(canvas_api)

from api import routes
