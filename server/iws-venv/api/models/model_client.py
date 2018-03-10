#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))

    def __init__(self, name):
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class ClientSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Client
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
