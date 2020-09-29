import fakeredis
import pytest
from api import CanvasAPI


@pytest.fixture
def app(mocker):
    """
    Set up a Flask App instance for testing.
    Create a Redis mock to abstract the tests from the actual Redis instance.
    """
    server = fakeredis.FakeServer()
    fake_redis = fakeredis.FakeStrictRedis(server=server)
    mocker.patch('redis.StrictRedis', return_value=fake_redis)

    flask_app = CanvasAPI.create_app('config.TestingConfig')
    yield flask_app


@pytest.fixture
def client(app):
    """
    Create a Flask test client instance to make test API calls.
    """
    test_client = app.test_client()
    return test_client
