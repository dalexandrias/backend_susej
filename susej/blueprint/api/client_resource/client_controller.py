from flask import Blueprint, request
from flask_restx import Api, Resource
from susej.schemas.client_schemas import ClientSchemas

from susej.services.client_service import ClientService

bp = Blueprint('client', __name__, url_prefix='/client/api/v1')
api = Api(bp, version='1.0', title='Client API', description='API para controle dos clientes')
client_ns = api.namespace('client', description='Controle do fluxo das operações para os clientes')
client_schemas = ClientSchemas(api)
client_service = ClientService()


@client_ns.route('/')
class CreateClient(Resource):
    """Realiza o controle das rotas POST e GET

    Args:
        Resource (_type_): Herda a lib flask restx
    """
    
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
    
    @client_ns.expect(client_schemas.client(), validate=True)
    @client_ns.marshal_with(client_schemas.out_client(), code=201, envelope='Client')
    def post(self):
        client_in = request.get_json()
        
        return client_service.save_client(client_in)

    @client_ns.marshal_with(client_schemas.client(), code=200, envelope='Client')
    def get(self):
        return client_service.get_all_client()
    
@client_ns.route('/<int:id>')
@client_ns.param('id', description='Id para identificação do cliente')
class ClientId(Resource):
    
    @client_ns.expect(client_schemas.client(), validate=True)
    @client_ns.marshal_with(client_schemas.out_client(), code=200)
    def put(self, id: int):
        return client_service.update_client(request.get_json(), id)
        
    def delete(self):
        ...
    
