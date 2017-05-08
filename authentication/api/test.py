from unittest.case import TestCase

from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/register/')


class AuthRegisterView(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test1@example.com',
            'username': 'test1',
            'first_name': 'test1',
            'last_name': 'test1',
            'password': '123456789',
            'confirm_password': '123456789',
        }
        self.user_data2 = {
            'email': 'test2@example.com',
            'username': 'testZ',
            'first_name': 'testZ',
            'last_name': 'test2',
            'password': '123456789',
            'confirm_password': '123456789',
        }
        self.user_data_wrong_confirm_password = {
            'email': 'test2@example.com',
            'username': 'testZ',
            'first_name': 'testZ',
            'last_name': 'test2',
            'password': '123456789',
            'confirm_password': '123456789',
        }

        self.message_confirm_password_wrong = 'The passwords have to the be the same'
