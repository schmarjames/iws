#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_client import Client, ClientSchema
from api.models.model_product_area import ProductArea, ProductAreaSchema
from api.models.model_priority import Priority, PrioritySchema
from api.models.model_feature import Feature, FeatureSchema


route_path_general = Blueprint("route_path_general", __name__)

## CLIENTS
@route_path_general.route('/v1.0/clients', methods=['POST'])
def create_client():
    try:
        data = request.get_json()
        client_schema = ClientSchema()
        client, error = client_schema.load(data)
        result = client_schema.dump(client.create()).data
        return response_with(resp.SUCCESS_200, value={"client": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

@route_path_general.route('/v1.0/clients', methods=['GET'])
def get_all_clients():
    fetched = Client.query.all()
    client_schema = ClientSchema(many=True, only=['id', 'name'])
    clients, error = client_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"clients": clients})

## PRODUCT AREA
@route_path_general.route('/v1.0/product-area', methods=['POST'])
def create_product_area():
    try:
        data = request.get_json()
        product_area_schema = ProductAreaSchema()
        product_area, error = product_area_schema.load(data)
        result = product_area_schema.dump(product_area.create()).data
        return response_with(resp.SUCCESS_200, value={"productArea": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

@route_path_general.route('/v1.0/product-area', methods=['GET'])
def get_all_product_area():
    fetched = ProductArea.query.all()
    product_area_schema = ProductAreaSchema(many=True, only=['id', 'area_type'])
    product_area, error = product_area_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"productArea": product_area})

## PRIORITY
@route_path_general.route('/v1.0/priorities', methods=['POST'])
def create_priority():
    try:
        data = request.get_json()
        priority_schema = PrioritySchema()
        priority, error = priority_schema.load(data)
        result = priority_schema.dump(priority.create()).data
        return response_with(resp.SUCCESS_200, value={"priority": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

@route_path_general.route('/v1.0/priorities', methods=['GET'])
def get_all_priorities():
    fetched = Priority.query.all()
    priority_schema = PrioritySchema(many=True, only=['id', 'number', 'definition'])
    priorities, error = priority_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"priorities": priorities})

## FEATURES
@route_path_general.route('/v1.0/features', methods=['POST'])
def create_feature():
    try:
        data = request.get_json()
        print(request)
        feature_schema = FeatureSchema()
        feature, error = feature_schema.load(data)
        result = feature_schema.dump(feature.create()).data
        return response_with(resp.SUCCESS_200, value={"feature": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

@route_path_general.route('/v1.0/features', methods=['GET'])
def get_all_features():
    fetched = Feature.query.all()
    feature_schema = FeatureSchema(many=True)
    features, error = feature_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"features": features})
