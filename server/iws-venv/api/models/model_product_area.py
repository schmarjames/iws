#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class ProductArea(db.Model):
    __tablename__ = 'productAreas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area_type = db.Column(db.String(16))

    def __init__(self, area_type):
        self.area_type = area_type

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class ProductAreaSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = ProductArea
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    area_type = fields.String(required=True)
