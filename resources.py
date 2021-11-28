from flask_restful import Resource
from flask import request
from models import db, Product, Offer
from schemas import validate_data, product_schema_list, product_schema_no_name, product_schema_relation, product_schema


class ProductList(Resource):
    def get(self):
        products = Product.query.all()
        return product_schema_list.dump(products), 200

    def post(self):
        data = validate_data(request.get_json(), product_schema)
        product = Product(**data)
        print(product)
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product), 201


class ProductRes(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return product_schema.dump(product)

    def patch(self, product_id):
        product = Product.query.get_or_404(product_id)
        data = validate_data(request.json(), product_schema_no_name)

        for x, y in data.items():
            setattr(product, x, y)
        db.session.commit()
        return product_schema.dump(product)

    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return '', 204
