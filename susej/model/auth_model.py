import datetime
from datetime import datetime

from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin
from susej.extension.database import db

migrate = Migrate()


class User(db.Model, SerializerMixin):
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    creation_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, **kwargs) -> None:
        self.email = kwargs['email']
        self.password = kwargs['password']

    def __repr__(self) -> str:
        return f"Login {self.email}"



def init_app(app):
    migrate.init_app(app, db)
