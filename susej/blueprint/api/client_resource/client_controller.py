from flask import Blueprint, request
from flask_restx import Api, Namespace, Resource
from susej.exceptions.handler_error import handler_error_ns
from susej.schemas.client_schemas import ClientSchemas

from susej.services.client_service import ClientService

bp = Blueprint('client', __name__, url_prefix='/client/api/v1')
api_client = Api(bp, version='1.0', title='Client API',
          description='API para controle dos clientes')

client_ns = Namespace(
    'client', description='Controle do fluxo das operações para os clientes')

# Registro dos namespace na Api
api_client.add_namespace(client_ns)
api_client.add_namespace(handler_error_ns) 


# Injeção dos serviços
client_schemas = ClientSchemas(api_client)
client_service = ClientService()


@client_ns.route('/')
class CreateClient(Resource):
    """Realiza o controle das rotas POST e GET

    Args:
        Resource (_type_): Herda a lib flask restx
    """
    
    @client_ns.expect(client_schemas.client(), validate=True)
    @client_ns.marshal_with(client_schemas.out_client(), code=201, envelope='Client')
    def post(self): 
        return client_service.save_client(request.get_json())

    @client_ns.marshal_with(client_schemas.client(), code=200, envelope='Client')
    def get(self):
        return client_service.get_all_client()


@client_ns.route('/<int:id>')
@client_ns.param('id', description='Id para identificação do cliente')
class ClientId(Resource):
    """Realiza o controle das rotas PUT e DELETE

    Args:
        Resource (_type_): Herda a lib flask restx
    """

    @client_ns.expect(client_schemas.client(), validate=True)
    @client_ns.marshal_with(client_schemas.out_client(), code=200)
    def put(self, id: int):
        return client_service.update_client(request.get_json(), id)

    @client_ns.marshal_with(client_schemas.out_client(), code=200)
    def delete(self, id: int):
        return client_service.delete_client(id)
