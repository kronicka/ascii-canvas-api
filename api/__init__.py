from factory import FlaskAppFactory


class CanvasAPI(FlaskAppFactory):
    """
    A class representing the Canvas Application.
    """
    @classmethod
    def register_blueprints(cls, app):
        """
        Overriding this method to register the Blueprint specific to the Canvas API.
        """
        from api.blueprints import canvas_api
        app.register_blueprint(canvas_api)
