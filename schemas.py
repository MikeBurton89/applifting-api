from marshmallow import ValidationError, Schema, fields
from flask import abort


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(allow_none=True)


class ProductSchemaRelation(ProductSchema):
    id = fields.Function(lambda obj: str(obj.uuid))


class OfferSchema(Schema):
    id = fields.Int()
    price = fields.Int()
    items_in_stock = fields.Int()


product_schema = ProductSchema()
# this schema allows to update a product without the need to digit or change the name---------------
product_schema_no_name = ProductSchema(partial=('name'))
product_schema_list = ProductSchema(many=True)
product_schema_relation = ProductSchemaRelation()
offers_schema = OfferSchema()


def validate_data(raw_data: dict, schema: Schema) -> dict:
    if not raw_data:
        return abort(400, {'message': 'no input provided'})
    try:
        return schema.load(raw_data)
    except ValidationError:
        return abort(422, {'message': ValidationError.messages})
