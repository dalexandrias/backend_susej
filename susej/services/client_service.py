from http import HTTPStatus
import json

import validators
from susej.exceptions.error import ClientError
from susej.commands_dml.commands import commit_session, delete_one_by_id_client, get_all_client, get_one_by_email, insert_table, get_one_by_id_client, update_client
from susej.constants.status_return import CREATED_CLIENT, DELETE_CLIENT, EMAIL_ALREADY_EXISTS, EMAIL_INVALID, ERROR, ID_NOT_FOUND, SUCCESS, UPDATE_CLIENT
from susej.model.client_model import Client, ClientAddress


class ClientService(object):
    """Executa os serviços do cliente, criando, atualizando ou deletando.

    Args:
        object (_type_): _description_
    """

    def __init__(self) -> None:
        pass

    def save_client(self, client_body: json) -> json:

        client_in = Client(**client_body)

        client_email = get_one_by_email(client_in)
        if not client_email:
            if validators.email(client_in.email):
                insert_table(client_in)
                commit_session()

                return {
                    "status": SUCCESS,
                    "message": CREATED_CLIENT
                }, HTTPStatus.CREATED
            else:
                raise ClientError(EMAIL_INVALID)

        else:
            raise ClientError(EMAIL_ALREADY_EXISTS)

    def update_client(self, client_body: json, id: int) -> json:

        client = get_one_by_id_client(id)
        if client:
            if validators.email(client_body['email']):
                client_address = client_body['address_data']
                del client_body['address_data']
                update_client(Client, client_body, id)

                for address in client_address:
                    id_address = address['id']
                    update_client(ClientAddress, address, id_address)

                commit_session()

                return {
                    "status": SUCCESS,
                    "message": UPDATE_CLIENT
                }, HTTPStatus.CREATED
            else:
                raise ClientError(EMAIL_INVALID)
        else:
            raise ClientError(ID_NOT_FOUND)

    def get_all_client(self) -> list[Client]:
        return get_all_client()

    def delete_client(self, id: int) -> json:
        delete_one_by_id_client(id)
        commit_session()
        return {
            "status": SUCCESS,
            "message": DELETE_CLIENT
        }, HTTPStatus.CREATED
