from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource
from susej.constants.status_return import ERROR
from susej.model.auth_model import User
from susej.schemas.user_schemas import UserSchema
from susej.services.auth_services import AuthService

bp = Blueprint('auth', __name__, url_prefix='/auth/api/v1')
api = Api(bp, version='1.0', title='Auth API',
          description='API controle dos usuarios')
auth_ns = api.namespace('auth', description='Autenticação dos usuarios')
user_schemas = UserSchema(api)


@auth_ns.route('/user')
class CreateUser(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.auth_service = AuthService()

    @auth_ns.expect(user_schemas.new_user(), validate=True)
    @auth_ns.marshal_with(user_schemas.out_user(), code=201, envelope='User')
    def post(self):
        """Realiza o registro de um novo usuario

        Returns:
            Json: status, message
        """
        try:
            user_in = request.get_json()
            user = User(**user_in)

            return self.auth_service.save_user(new_user=user)
        except Exception as error:
            return {
                "status": ERROR,
                "message": f"{error}",
            }

    @auth_ns.expect(user_schemas.update_user(), validate=True)
    @auth_ns.marshal_with(user_schemas.out_user(), code=200, envelope='User')
    def put(self):
        try:
            user_in = request.get_json()

            return self.auth_service.user_update(update_user=user_in)
        except Exception as error:
            return {
                "status": ERROR,
                "message": f"{error}"
            }
