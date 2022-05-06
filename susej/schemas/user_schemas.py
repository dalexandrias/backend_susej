from flask_restx import Api, fields


class UserSchema(object):
    def __init__(self, api: Api) -> None:
        self.api = api

    def new_user(self):
        return self.api.model(
            'User', {
                "email": fields.String(description=u'Inserir e-mail para cadastro', required=True),
                "password": fields.String(description=u'Inserir senha para acesso a conta', required=True)
            }
        )
        
    def update_user(self):
        return self.api.model(
            'User Update', {
                "email": fields.String(description=u'E-mail cadastrado', required=True),
                "new_email": fields.String(description=u'Novo e-mail', required=True),
                "password": fields.String(description=u'Nova senha', required=True)
                }
        )
        
    def out_user(self):
        return self.api.model(
            'Out User', {
                "status": fields.String(description='Status de saida erro ou success', required=True),
                "message": fields.String(description='Mensagem de retorno', required=True)
            }
        )
