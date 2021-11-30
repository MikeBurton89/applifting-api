from typing import Callable
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import uuid


db = SQLAlchemy()


class IdModel(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)


class OffersMS(IdModel):
    access_token = db.Column(db.Integer,
                             unique=True, nullable=False)

    @classmethod
    def get_access_token(cls, extract_access_token: Callable[[], str]):
        om = db.session.query(cls).first()
        if om is None:
            access_token = extract_access_token()
            om = cls(access_token=access_token)
            db.session.add(om)
            db.session.commit()
        return str(om.access_token)


class Offer(IdModel):
    # the Offer model has a many to one relationship to Product through the product.id foreign key
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    id_external = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer)
    items_in_stock = db.Column(db.Integer)
    __table_args__ = (
        UniqueConstraint('product_id', 'id_external'),
    )


class Product(IdModel):
    uuid = db.Column(db.Integer, default=uuid.uuid4,
                     unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    offers = db.relationship('Offer', backref='product', lazy=True)
