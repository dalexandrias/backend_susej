from susej.extension.database import db
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    __tablename__ = 'PRODUCTS'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    store_owner = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, price, store_owner, creation_date):
        self.name = name
        self.price = price
        self.store_owner = store_owner
        self.creation_date = creation_date

    def __repr__(self):
        return f"Product {self.name}"
