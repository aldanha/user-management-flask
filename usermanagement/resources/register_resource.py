from flask_restful import Resource, reqparse
from database import db
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('password', type=str, required=True, help='Password is required')


class RegisterResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        user = User.query.filter_by(username=username).first()
        if user:
            return {'message': 'Username already exists'}, 409

        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201
