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


def commit_session() -> None:
    db.session.commit()
    db.session.close()

def get_all_client() -> list[Client]:
    return db.session.query(Client).join(Client.address).all()

def get_one_by_email(table: object):
    return table.query.filter_by(email=table.email).first()
