import json
from flask import Response


def test_main_page(app, client):
    """
    Test the access to the Main Page of the application.
    """
    res = client.get('/')
    assert res.status_code == 200


def test_put_paint_rectangle(app, client):
    """
    A simple API Test for the Paint Rectangle Endpoint.
    """
    endpoint_url: str = '/api/v1/canvas/paint'

    headers: dict = {
        'Content-Type': 'application/json'
    }
    payload: dict = {
        "x": 3,
        "y": 2,
        "width": 5,
        "height": 3,
        "fill_symbol": "x",
        "outline_symbol": "@"
    }

    response: Response = client.put(
        endpoint_url, headers=headers, data=json.dumps(payload)
    )

    assert response.status_code == 200


def test_put_fill_area(app, client):
    """
    A simple API Test for the Fill an Area Endpoint.
    """
    endpoint_url: str = '/api/v1/canvas/fill'

    headers: dict = {
        'Content-Type': 'application/json'
    }
    payload: dict = {
        "x": 5,
        "y": 6,
        "fill_symbol": "-"
    }

    response: Response = client.put(
        endpoint_url, headers=headers, data=json.dumps(payload)
    )

    assert response.status_code == 200
