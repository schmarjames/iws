#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.database import db
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_client import Client, ClientSchema
from api.models.model_product_area import ProductArea, ProductAreaSchema
from api.models.model_priority import Priority, PrioritySchema
from api.models.model_feature import Feature, FeatureSchema


route_path_general = Blueprint("route_path_general", __name__)
modelMap = {
    "feature" : {
        "model": Feature,
        "schema": FeatureSchema
    },
    "priority" : {
        "model": Priority,
        "schema": PrioritySchema
    },
    "product_area" : {
        "model": ProductArea,
        "schema": ProductAreaSchema
    },
    "client" : {
        "model": Client,
        "schema": ClientSchema
    }
}

def queryAllData(modelType, only=[]):
    fetched = modelMap[modelType]["model"].query.all()
    model_type_schema = modelMap[modelType]["schema"](many=True, only=only)
    return model_type_schema.dump(fetched)

def querySpecificData(modelType, searchBy):
    clientObj = modelMap[modelType]["model"].query.filter_by(id=searchBy)
    model_type_schema = modelMap[modelType]["schema"](many=True)
    return model_type_schema.dump(clientObj)

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
    clients, error = queryAllData('client', ['id', 'name'])
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
    product_area, error = queryAllData('product_area', ['id', 'area_type'])
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
    priorities, error = queryAllData('priority', ['id', 'number', 'definition'])
    return response_with(resp.SUCCESS_200, value={"priorities": priorities})

## FEATURES
@route_path_general.route('/v1.0/features', methods=['POST'])
def create_feature():
    try:

        ## store new feature
        data = request.get_json()
        print(data)
        feature_schema = FeatureSchema()
        feature, error = feature_schema.load(data)
        result = feature_schema.dump(feature.create()).data

        ## check if client id exist
        avail_client = Client.query.filter_by(id=data['client_id'])
        client_schema = ClientSchema(many=True)
        client, error = client_schema.dump(avail_client)

        ## reorder features of client by priority
        ## Can be extracted into another class
        if not (client is None):
            client_features = Feature.query.filter_by(client_id=data['client_id']).order_by(Feature.priority.asc())
            feature_schema = FeatureSchema(many=True)
            cl_features, error = feature_schema.dump(client_features)

            if not (cl_features is None):
                for i, j in enumerate(cl_features):
                    currentPriorityVal = j['priority']

                    nextIndex = i+1
                    if (len(cl_features) != nextIndex):
                        nextPriorityVal = cl_features[nextIndex]['priority']
                        if (nextPriorityVal == currentPriorityVal):
                            increment = nextPriorityVal+1
                            cl_features[nextIndex]['priority'] = increment
                            client_features[nextIndex].priority = increment
                db.session.commit()

        return response_with(resp.SUCCESS_200, value={"feature": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)

@route_path_general.route('/v1.0/features', methods=['DELETE'])
def delete_feature():
    data = request.get_json()

    fetched = Feature.query.filter_by(id=data['id']).one()
    db.session.delete(fetched)
    db.session.commit()

    features, error = queryAllData('feature')

    for feature in features:
        client, error = querySpecificData('client', feature['client_id'])
        feature['client'] = client.pop()['name']

        product_area, error = querySpecificData('product_area', feature['product_area_id'])
        feature['product_area'] = product_area.pop()['area_type']

    return response_with(resp.SUCCESS_200, value={"features": features})

@route_path_general.route('/v1.0/features', methods=['GET'])
def get_all_features():
    features, error = queryAllData('feature')

    for feature in features:
        client, error = querySpecificData('client', feature['client_id'])
        feature['client'] = client.pop()['name']

        product_area, error = querySpecificData('product_area', feature['product_area_id'])
        feature['product_area'] = product_area.pop()['area_type']

    return response_with(resp.SUCCESS_200, value={"features": features})
