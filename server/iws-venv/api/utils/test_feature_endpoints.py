#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import json
from api.utils.factory import create_app
from api.utils.database import db
from api.utils.config import TestingConfig


class FeatureEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app(TestingConfig)
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        db.session.close_all()
        db.drop_all()

    def test_getting_features(self):
        response = self.app.get('/api/v1.0/features', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_new_feature(self):
        payload = {
        	"title": "Multiple Domains",
        	"description": "User should be able to select and add multiple domains to there cart.",
        	"client_id": 1,
        	"priority_id": 3,
        	"target_date": "4/27/2018",
        	"product_area_id": 2
        }
        response = self.app.post('/api/v1.0/features', data=payload)
        self.assertEqual(response.status_code, 200)
