from flask import Blueprint, Flask
from flask_restx import Api
from .product_controller import ProductService

bp = Blueprint("product", __name__, url_prefix='/product/api/v1')
api = Api(bp, version='1.0', title='Product', description='API controle dos usuarios')

def init_app(app: Flask):
    api.add_resource(ProductService, "/product/")
    app.register_blueprint(bp)
