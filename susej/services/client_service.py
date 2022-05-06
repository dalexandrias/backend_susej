import json
from susej.commands_dml.commands import commit_session, insert_table, select_table
from susej.constants.status_return import CREATED_CLIENT, SUCCESS
from susej.model.client_model import Client, ClientAddress


class ClientService(object):
    def __init__(self) -> None:
        pass

    def save_client(self, client_body: json) -> json:
        
        client_in = Client(**client_body)
        client_address_in = ClientAddress(**client_in.address)
        
        client_in.client_address.append(client_address_in)
        
        insert_table(client_in)
        commit_session()

        return {
            "status": SUCCESS,
            "message": CREATED_CLIENT
        }
        
    def get_all_client(self) -> json:
        return select_table(Client)
