from susej.extension.database import db


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
