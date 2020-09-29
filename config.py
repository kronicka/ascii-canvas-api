from pathlib import Path


class Config(object):
    """
    Generic Flask App configuration object.
    """
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = True

    FLASK_HOST = 'localhost'
    FLASK_PORT = 1337

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379

    CANVAS_FILE_PATH: Path = Path(__file__).parent / 'api/canvas/canvas.csv'


class DockerConfig(Config):
    """
    Flask config variables for Docker containers.
    """
    REDIS_HOST = 'redis'
    FLASK_HOST = '0.0.0.0'


class DevelopmentConfig(Config):
    """
    Flask config variables for local development.
    """
    ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    """
    Flask config variables for running auto-tests.
    """
    TESTING = True
    CANVAS_FILE_PATH: Path = Path(__file__).parent / 'tests/fixtures/test_canvas.csv'
