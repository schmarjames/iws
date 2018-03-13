#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Feature(db.Model):
    __tablename__ = 'features'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    product_area_id = db.Column(db.Integer, db.ForeignKey('productAreas.id'))


    def __init__(self, title, description, client_id, priority, target_date, product_area_id):
        self.title = title
        self.description = description
        self.client_id = client_id
        self.priority = priority
        self.target_date = target_date
        self.product_area_id = product_area_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class FeatureSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Feature
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    client_id = fields.Number(required=True)
    priority = fields.Number(required=True)
    target_date = fields.DateTime(required=True)
    product_area_id = fields.Number(required=True);
