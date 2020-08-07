from flask_marshmallow import Schema
from marshmallow.fields import Nested, Number, Str
from api.schema.transaction import TransactionSchema


class NameSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ["first", "middle", "last"]

