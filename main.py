from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import db
from resources import ProductRes, ProductList
from offerMicroService import OFFERS_URL, OffersMsClient


def bad_request(e):
    return {'message': 'Bad request'}, 400


def not_found(e):
    return {'message': 'Not found'}, 404


def internal_error(e):
    db.session.rollback()
    return {'message': 'Internal Server error'}, 500


def create_app(conf: str = 'DevConf'):
    app = Flask(__name__)

    app.config.from_object(f'config.{conf}')

    app.register_error_handler(400, bad_request)
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_error)

    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    api = Api(app)

    api.add_resource(ProductList, '/products/')
    api.add_resource(ProductRes, '/products/<int:product_id>/')

    return app
