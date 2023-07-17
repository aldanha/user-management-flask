import jwt
from flask import current_app

def decode_token(token):
    try:
        
        secret_key = current_app.config['SECRET_KEY']
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None  
    except jwt.InvalidTokenError:
        return None  
