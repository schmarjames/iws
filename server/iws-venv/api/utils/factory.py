#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys
from flask import Flask
from flask import jsonify
from api.utils.database import db
from api.routes.standard_path import standard_path

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    app.register_blueprint(standard_path, url_prefix='/api')
    db.init_app(app)
    with app.app_context():
        # from api.models import *
        db.create_all()

    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s',
                        level=logging.DEBUG)
    return app
