from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from models import db
from resources import Product, ProductList
import os


def bad_request(e):
    return {'message': 'Bad request'}, 400


def not_found(e):
    return {'message': 'Not found'}, 404


def internal_error(e):
    db.session.rollback()
    return {'message': 'Internal Server error'}, 500

# TODO add production and testing Configurations


def create_app(conf: str = 'DevConf'):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(f'config.{conf}')

    app.register_error_handler(400, bad_request)
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_error)

    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    api.add_resource(ProductList, '/products/')
    api.add_resource(Product, '/products/<int:product_id>/')

    return app
