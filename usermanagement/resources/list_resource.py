from flask import request
from flask_restful import Resource
from database import db
from models import User
from token_utils import decode_token


class ListResource(Resource):
    def get(self):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return {'message': 'Missing authorization token'}, 401

        try:
            token = auth_header.split()[1]
            decoded_token = decode_token(token)
            if not decoded_token:
                return {'message': 'Invalid or expired authorization token'}, 401

            user_id = decoded_token.get('user_id')
            if not user_id:
                return {'message': 'Invalid authorization token'}, 401

            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 401


        except IndexError:
            return {'message': 'Invalid authorization token'}, 401

        users = User.query.all()
        user_list = [{'username': user.username} for user in users]
        return {'users': user_list}, 200
