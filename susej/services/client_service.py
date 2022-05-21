from http import HTTPStatus
import json

import validators
from susej.commands_dml.commands import commit_session, get_all_client, get_one_by_email, insert_table, select_table
from susej.constants.status_return import CREATED_CLIENT, EMAIL_ALREADY_EXISTS, EMAIL_INVALID, ERROR, SUCCESS
from susej.model.client_model import Client, ClientAddress


class ClientService(object):
    def __init__(self) -> None:
        pass

    def save_client(self, client_body: json) -> json:
        
        client_in = Client(client_body['nome'], client_body['sobrenome'], client_body['email'])

        client_email = get_one_by_email(client_in)
        if not client_email:
            if validators.email(client_in.email):

                [client_in.address.append(ClientAddress(**client_address)) for client_address in client_body.address]
        
                insert_table(client_in)
                commit_session()

                return {
                    "status": SUCCESS,
                    "message": CREATED_CLIENT
                }, HTTPStatus.CREATED
            else:
                return {
                    "status": ERROR,
                    "message": EMAIL_INVALID
                }, HTTPStatus.BAD_REQUEST

        else:
            return {
                "status": ERROR,
                "message": EMAIL_ALREADY_EXISTS
            }, HTTPStatus.BAD_REQUEST
        
    def get_all_client(self):
        return get_all_client()
