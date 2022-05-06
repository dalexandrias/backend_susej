from flask_migrate import Migrate
from sqlalchemy import ForeignKey
from sqlalchemy_serializer import SerializerMixin
from susej.extension.database import db

migrate = Migrate()


class ClientAddress(db.Model, SerializerMixin):
    __tablename__ = 'CLIENT_ADDRESS'

    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(200), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    numero = db.Column(db.String(50), nullable=False)
    complemento = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(200), nullable=False)
    id_client = db.Column(db.Integer, ForeignKey('CLIENT.id'))

    def __init__(
        self,
        rua: str,
        bairro: str,
        numero: str,
        complemento: str,
        cidade: str,
        estado: str,
        cep: str
    ) -> None:
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __repr__(self) -> str:
        return f"Rua {self.rua}"


class Client(db.Model, SerializerMixin):
    __tablename__ = 'CLIENT'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    client_address = db.relationship('ClientAddress', backref='CLIENT')

    def __init__(
        self,
        nome: str,
        sobrenome: str,
        email: str,
        address: ClientAddress
    ) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.address = address

    def __repr__(self) -> str:
        return f"Client {self.nome}"


def init_app(app):
    migrate.init_app(app, db)
