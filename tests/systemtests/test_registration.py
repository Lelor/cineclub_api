from unittest import TestCase

from flask import url_for

from app import create_app
from app.models import db


class TestRegistration(TestCase):
    def setUp(self):
        self.app = create_app('config/test.py')
        self.client = self.app.test_client()
        context = self.app.app_context()
        context.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_create_user_route_should_save_in_database(self):
        user_data = {
            'username': 'testuser',
            'password': 'secret',
            'email': 'user@test.dev',
            'birthdate': '2019-05-27T16:30:15.970340'
        }
        res = self.client.post(url_for('registration.sign_up'), json=user_data)
        import ipdb; ipdb.set_trace()
        self.assertEqual(res.status_code, 201)
