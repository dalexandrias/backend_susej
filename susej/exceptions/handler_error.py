from flask_restx import Namespace
from susej.exceptions.error import AuthError

handler_error_ns = Namespace('handler_error', description='Manipulação das exceptions')

class HandlerException():
    
    @handler_error_ns.errorhandler(AuthError)
    def handler_client_error(error):
        return {"status": "Error", "message": error.args[0]}, error.code
