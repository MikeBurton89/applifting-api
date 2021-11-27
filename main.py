from flask import Flask, abort
from flask_restful import Api, Resource, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, ValidationError, fields
import models
from resources import Product, ProductList


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


api.add_resource(ProductList, '/products/')
api.add_resource(Product, '/products/<int:product_id>/')


if __name__ == '__main__':
    app.run(debug=True)
