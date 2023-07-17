from flask_restful import Resource, reqparse
from token_utils import decode_token
from models import User
from database import db
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('password', type=str, required=True, help='Password is required')


class RemoveUserResource(Resource):
    def delete(self):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {'message': 'Missing authorization token'}, 401

        try:
            token = auth_header.split()[1]
            decoded_token = decode_token(token)
            if not decoded_token:
                return {'message': 'Invalid or expired authorization token'}, 401


        except IndexError:
            return {'message': 'Invalid authorization token'}, 401

        args = parser.parse_args()
        username = args['username']
        password = args['password']

        user = User.query.filter_by(username=username, password=password).first()
        if not user:
            return {'message': 'Invalid username or password'}, 401

        db.session.delete(user)
        db.session.commit()

        return {'message': 'User removed successfully'}, 200
