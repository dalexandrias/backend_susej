import json
from typing import Any
from susej.extension.database import db
from susej.model.client_model import Client, ClientAddress


def insert_table(table: object) -> None:
    db.session.add(table)


def select_table(table: object) -> list:
    return table.query.all()


def delete_table(all=False, **args) -> None:
    if all:
        db.session.query(args['table']).delete()
    else:
        user_id = db.session.get(args['table'], id)

    db.session.commit()
    db.session.close()
    
def update_client(table: object, values: dict, id: int) -> None:
    db.session.query(table).filter(table.id == id).update(values, synchronize_session='fetch')


def commit_session() -> None:
    db.session.commit()
    db.session.close()

def get_all_client() -> list[Client]:
    return db.session.query(Client).join(Client.address_data).all()

def get_one_by_email(table: object):
    return table.query.filter_by(email=table.email).first()

def get_one_by_id_client(id: int) -> Client:
    return db.session.query(Client).get(id)

def delete_one_by_id_client(id: int) -> None:
    client = Client.query.filter_by(id=id).first()
    ClientAddress.query.filter_by(id_client=client.id).delete()
    db.session.delete(client)
