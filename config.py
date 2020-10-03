from pathlib import Path


class Config(object):
    """
    Generic Flask App configuration object.
    """
    DEBUG: bool = False
    TESTING: bool = False
    TEMPLATES_AUTO_RELOAD: bool = True

    FLASK_HOST: int = 'localhost'
    FLASK_PORT: int = 1337

    REDIS_HOST: int = 'localhost'
    REDIS_PORT: int = 6379

    CANVAS_FILE_PATH: Path = Path(__file__).parent / 'api/canvas/canvas.csv'


class DockerConfig(Config):
    """
    Flask config variables for Docker containers.
    """
    REDIS_HOST: str = 'redis'
    FLASK_HOST: str = '0.0.0.0'


class DevelopmentConfig(Config):
    """
    Flask config variables for local development.
    """
    ENV: str = 'development'
    DEBUG: bool = True


class TestingConfig(Config):
    """
    Flask config variables for running auto-tests.
    """
    TESTING: bool = True
    CANVAS_FILE_PATH: Path = Path(__file__).parent / 'tests/fixtures/test_canvas.csv'
