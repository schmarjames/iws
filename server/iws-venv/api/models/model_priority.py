#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Priority(db.Model):
    __tablename__ = 'priorities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    definition = db.Column(db.String(16))

    def __init__(self, number, definition):
        self.number = number
        self.definition = definition

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class PrioritySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Priority
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    number = fields.Number(required=True)
    definition = fields.String(required=True)
