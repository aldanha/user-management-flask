import unittest
from flask import Flask
from flask_testing import TestCase
from app import app


class BaseTestCase(TestCase):
    def create_app(self):
        return app


class LoginTestCase(BaseTestCase):
    def test_login_success(self):
        response = self.client.post('/login', json={'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_login_failure(self):
        response = self.client.post('/login', json={'username': 'nonexistent', 'password': 'password'})
        self.assertEqual(response.status_code, 401)
        self.assertNotIn('token', response.json)


class RegisterTestCase(BaseTestCase):
    def test_register_success(self):
        response = self.client.post('/register', json={'username': 'newuser', 'password': 'password'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'User registered successfully')

    def test_register_failure(self):
        response = self.client.post('/register', json={'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['message'], 'Username already exists')


class ListTestCase(BaseTestCase):
    def test_list_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.json)


class AddUserTestCase(BaseTestCase):
    def test_add_user_success(self):
        response = self.client.post('/users/add', json={'username': 'newuser', 'password': 'password'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'User added successfully')

    def test_add_user_failure(self):
        response = self.client.post('/users/add', json={'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json['message'], 'Username already exists')


class RemoveUserTestCase(BaseTestCase):
    def test_remove_user_success(self):
        response = self.client.delete('/users/remove', json={'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'User removed successfully')

    def test_remove_user_failure(self):
        response = self.client.delete('/users/remove', json={'username': 'nonexistent', 'password': 'password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], 'Invalid username or password')


if __name__ == '__main__':
    unittest.main()

