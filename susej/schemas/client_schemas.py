from flask_restx import Api, fields


class ClientSchemas(object):
    def __init__(self, api: Api) -> None:
        self.api = api

    def new_client(self):
        address_model = self.api.model(
            'Client Address', {
                "rua": fields.String(description='rua do Cliente', required=True),
                "bairro": fields.String(description='bairro do Cliente', required=True),
                "numero": fields.String(description='numero do Cliente', required=True),
                "complemento": fields.String(description='complemento do Cliente', required=True),
                "cidade": fields.String(description='cidade do Cliente', required=True),
                "estado": fields.String(description='estado do Cliente', required=True),
                "cep": fields.String(description='cep do Cliente', required=True)
            }
        )
        
        client_model = self.api.model(
            'Client', {
                "id": fields.Integer(description='ID do cliente'),
                "nome": fields.String(description='Nome do Cliente', required=True),
                "sobrenome": fields.String(description='sobrenome do Cliente', required=True),
                "email": fields.String(description='E-mail do Cliente', required=True),
                "address": fields.List(fields.Nested(address_model))
            }
        )
        
        return client_model

    def out_client(self):
        return self.api.model(
            'Client Out', {
                "status": fields.String(description='Status de retorno', required=True),
                "message": fields.String(description='Mensagem de retorno', required=True)
            }
        )
