from flask_restful import Resource, reqparse
from database import db
from models import User
import jwt
import datetime

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('password', type=str, required=True, help='Password is required')


class LoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            
            secret_key = 'your-secret-key'  
            expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1) 

            token = jwt.encode({
                'user_id': user.id,
                'exp': expiration_time
            }, secret_key, algorithm='HS256')
            return {'token': token}, 200
        else:
            return {'message': 'Invalid username or password'}, 401
