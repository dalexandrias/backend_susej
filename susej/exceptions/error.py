from http import HTTPStatus


class ClientException(Exception):
    pass


class AuthError(ClientException):
    code = HTTPStatus.FORBIDDEN
    description = 'Autenticação falhou'
