#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.models.model_client import Client, ClientSchema


standard_path = Blueprint("standard_path", __name__)

success_obj = {
    'http_code': 200,
    'code': 'success'
}

failed_obj = {
    "http_code": 422,
    "code": "invalidField",
    "message": "Not all field names are valid."
}

## CLIENTS
@standard_path.route('/v1.0/clients', methods=['POST'])
def create_client():
    try:
        data = request.get_json()
        client_schema = ClientSchema()
        client, error = client_schema.load(data)
        result = client_schema.dump(client.create()).data
        return response_with(success_obj, value={"client": result})
    except Exception:
        return response_with(failed_obj)

@standard_path.route('/v1.0/clients', methods=['GET'])
def get_all_clients():
    fetched = Client.query.all()
    client_schema = ClientSchema(many=True, only=['id', 'name'])
    clients, error = client_schema.dump(fetched)
    return response_with(success_obj, value={"clients": clients})
