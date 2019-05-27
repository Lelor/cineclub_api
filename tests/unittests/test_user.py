from unittest import TestCase

from werkzeug import security

from app import create_app
from app.models import User



class TestSignUp(TestCase):
    """Sign up tests."""

    def setUp(self):
        self.app = create_app('config/test.py')
        context = self.app.app_context()
        context.push()
        self.user_data = {
            'username': 'testuser',
            'password': 'secret',
            'email': 'user@test.dev',
            'birthdate': '2019-05-27T16:30:15.970340'
        }
        self.test_user = User(**self.user_data)
        self.test_user.hash_password()

    def test_user_authentication_validates_correct_password_and_returns_jwt(self):
        token = self.test_user.authenticate('secret')
        self.assertTrue(token)

    def test_user_authentication_fails_with_wrong_password(self):
        token = self.test_user.authenticate('secret1')
        self.assertFalse(token)