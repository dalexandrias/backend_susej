from http import HTTPStatus


class ClientException(Exception):
    pass


class ClientError(ClientException):
    code = HTTPStatus.BAD_REQUEST
