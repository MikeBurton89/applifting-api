from flask_sqlalchemy import SQLAlchemy
from main import db


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
