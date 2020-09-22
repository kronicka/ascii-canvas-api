from flask import Blueprint
from flask_cors import CORS

canvas_api = Blueprint('canvas_api', __name__)
CORS(canvas_api)

from api import routes
