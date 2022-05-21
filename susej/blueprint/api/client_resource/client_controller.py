from flask import Blueprint, request
from flask_restx import Api, Resource
from susej.schemas.client_schemas import ClientSchemas

from susej.services.client_service import ClientService

bp = Blueprint('client', __name__, url_prefix='/client/api/v1')
api = Api(bp, version='1.0', title='Client API', description='API para controle dos clientes')
client_ns = api.namespace('client', description='Controle do fluxo das operações para os clientes')
client_schemas = ClientSchemas(api)


@client_ns.route('/')
class CreateClient(Resource):
    """Clase responsavel para gerenciar as rotas de entrada e saida"""
    
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.client_service = ClientService()
    
    @client_ns.expect(client_schemas.new_client(), validate=True)
    @client_ns.marshal_with(client_schemas.out_client(), code=200, envelope='Client')
    def post(self):
        client_in = request.get_json()
        
        return self.client_service.save_client(client_in)

    @client_ns.marshal_list_with(client_schemas.new_client(), code=200, envelope='Client')
    def get(self):
        return self.client_service.get_all_client()
        
    def put(self):
        ...
        
    def delete(self):
        ...
