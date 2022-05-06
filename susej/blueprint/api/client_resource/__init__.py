from flask import Flask
from susej.blueprint.api.client_resource.client_controller import bp


def init_app(app: Flask) -> None:
    app.register_blueprint(bp)
