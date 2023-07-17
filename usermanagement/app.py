from flask import Flask, request
from flask_restful import Api
from database import db
from resources.login_resource import LoginResource
from resources.register_resource import RegisterResource
from resources.list_resource import ListResource
from resources.add_user_resource import AddUserResource
from resources.remove_user_resource import RemoveUserResource

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

# Secret key for JWT token signing 
app.config['SECRET_KEY'] = 'your-secret-key'


@app.before_request
def create_tables():
    db.create_all()



api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')
api.add_resource(ListResource, '/users')
api.add_resource(AddUserResource, '/users/add')
api.add_resource(RemoveUserResource, '/users/remove')


if __name__ == '__main__':
    app.run(debug=True)
