from flask import Flask

from susej.blueprint.api import product_resource, login_resource, client_resource
from susej.extension import configuration, database
from susej.model import auth_model as auth_migrate
from susej.model import client_model as client_migrate


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    login_resource.init_app(app)
    product_resource.init_app(app)
    client_resource.init_app(app)
    
    # Atualiza as alterações das tabelas de dados
    auth_migrate.init_app(app)
    client_migrate.init_app(app)
