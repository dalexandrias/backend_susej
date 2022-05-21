import os
from flask import Flask


def init_app(app: Flask) -> None:
    """Realiza a configuração da aplicação, carregando as variaveis de ambiente

    Args:
        app (Flask): application Flask
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('HEROKU_POSTGRESQL_BLUE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

