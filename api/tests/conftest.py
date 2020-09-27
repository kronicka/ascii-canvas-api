import fakeredis
import pytest
from api import CanvasAPI


@pytest.fixture
def app(mocker):
    server = fakeredis.FakeServer()
    fake_redis = fakeredis.FakeStrictRedis(server=server)
    mocker.patch('redis.StrictRedis', return_value=fake_redis)

    flask_app = CanvasAPI.create_app()
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
