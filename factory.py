import os
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class FlaskAppFactory:
    """ A Factory class to create a configured Flask REST application object. """
    @classmethod
    def create_app(cls) -> Flask:
        """
        Create a Flask application object with the specified configs, extensions, and blueprints.
        """
        app = Flask(__name__)

        environment_config: str = os.environ.get('CONFIGURATION_ENV', 'config.Config')
        app.config.from_object(environment_config)

        CORS(app)

        cls.initialize_extensions(app)
        cls.register_blueprints(app)

        return app

    @classmethod
    def initialize_extensions(
            cls,
            app: Flask
    ) -> None:
        """
        Bind each Flask extension instance to the Flask application instance.
        """
        ma.init_app(app=app)

    @classmethod
    def register_blueprints(
            cls,
            app: Flask
    ) -> None:
        """
        Register Blueprints for appropriate route management.

        Without Blueprints, Flask won't be able to resolve the endpoints outside of the file containing the Application.
        Override this method to register each Blueprint with a specific Flask application instance.
        """
        pass
