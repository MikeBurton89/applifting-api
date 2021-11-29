from typing import Callable
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import UUID


db = SQLAlchemy()


class OffersMS(db.Model):
    access_token = db.Column(UUID(as_uuid=True),
                             unique=True, nullable=False)

    @classmethod
    def get_access_token(cls, extract_access_token: Callable[[], str]):
        om = db.session.query(cls).first()
        if om is None:
            access_token = extract_access_token()
            omr = cls(access_token=access_token)
            db.session.add(omr)
            db.session.commit()
        return str(omr.access_token)


class Offer(db.Model):
    # the Offer model has a many to one relationship to Product through the product.id foreign key
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    id_external = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer)
    items_in_stock = db.Column(db.Integer)
    db.PrimaryKeyConstraint(product_id, id_external)


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    offers = db.relationship('Offer', backref='product', lazy=True)
    db.PrimaryKeyConstraint(id)
