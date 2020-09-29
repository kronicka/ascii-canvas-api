import json
import os
import pytest

from config import TestingConfig
from flask import Response
from tests import params
from pathlib import Path


@pytest.fixture(autouse=True)
def remove_canvas_file_after_tests():
    """
    Removes the generated Test Canvas after the tests were run.
    """
    yield
    test_file_path: Path = TestingConfig.CANVAS_FILE_PATH
    os.remove(str(test_file_path))


def test_main_page(app, client):
    """
    Test the access to the Main Page of the application.
    """
    res = client.get('/')
    assert res.status_code == 200


@pytest.mark.parametrize(
    'payload_args, expected_status_code',
    [
        params.paint_rectangle_success_payload_1,
        params.paint_rectangle_success_payload_2,
        params.paint_rectangle_success_payload_3,
        params.paint_rectangle_fail_payload_1,
        params.paint_rectangle_fail_payload_2,
        params.paint_rectangle_fail_payload_3
    ]
)
def test_put_paint_rectangle(app, client, payload_args, expected_status_code):
    """
    A simple API Test for the Paint Rectangle Endpoint.
    """
    endpoint_url: str = '/api/v1/canvas/paint'

    headers: dict = {
        'Content-Type': 'application/json'
    }

    response: Response = client.put(
        endpoint_url, headers=headers, data=json.dumps(payload_args)
    )

    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    'payload_args, expected_status_code',
    [
        params.fill_success_payload_1,
        params.fill_success_payload_2,
        params.fill_fail_payload_1,
        params.fill_fail_payload_2
    ]
)
def test_put_fill_area(app, client, payload_args, expected_status_code):
    """
    A simple API Test for the Fill an Area Endpoint.
    """
    endpoint_url: str = '/api/v1/canvas/fill'

    headers: dict = {
        'Content-Type': 'application/json'
    }

    response: Response = client.put(
        endpoint_url, headers=headers, data=json.dumps(payload_args)
    )

    assert response.status_code == expected_status_code
