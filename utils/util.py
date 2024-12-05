import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify
import json
from urllib.request import urlopen
import os

SECRET_KEY = os.getenv('SECRET_KEY')

# Auth0 Configuration
AUTH0_DOMAIN = os.getenv('VITE_AUTH0_DOMAIN')
API_IDENTIFIER = os.getenv('API_IDENTIFIER')
ALGORITHMS = os.getenv('ALGORITHMS')

def get_current_user():
    token = request.headers.get('Authorization').split(' ')[1] # Get token from header
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        print("Payload", payload)
        neighbor_id = payload['sub']
        return neighbor_id
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

def encode_token(user_id): #original
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting an expiration date
        'iat': datetime.now(timezone.utc), #issued at
        'sub': user_id #subject, aka, who is the token for
    }

    token = jwt.encode(payload, SECRET_KEY,  algorithm='HS256')
    return token


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({"message": "Authorization header is missing"}), 401

        try:
            token = auth_header.split()[1]
            payload = verify_jwt(token)
            request.user = payload  # Attach user info to the request object
            return f(*args, **kwargs)
        except ValueError as e:
            return jsonify({"message": str(e)}), 401

    return wrapper


def user_validation(f): #validates and returns the user_id associated with the token
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers["Authorization"].split()[1]
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token is expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token"}), 401    
            return f(token_id=payload['sub'], *args, **kwargs)
        else:
            return jsonify({"message": "Authentication token missing"}), 401
        
    return wrapper


def encode_role_token(user_id, role_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1), #setting an expiration date
        'iat': datetime.now(timezone.utc), #issued at
        'sub': user_id, #subject, aka, who is the token for
        'admin': role_id
    }

    token = jwt.encode(payload, SECRET_KEY,  algorithm='HS256')
    return token


def admin_required(f): #f = the function our wrapper wraps around
    @wraps(f)
    def wrapper(*args, **kwargs): #when wrapping around a function we need to make sure its parameters make it through the wrapper
        token = None
        if 'Authorization' in request.headers: 
            try:
                token = request.headers['Authorization'].split()[1] 
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')# decoding the token with the same way we encoded it
                print("Payload", payload)
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token is expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid Token"}), 401
            if payload['admin']:
                return f(*args, **kwargs) #Calling our wrapped function
            else:
                return jsonify({"message": "Need Admin permissions"}), 401
        else:
            return jsonify({"message": "Authentication token missing"}), 401
    return wrapper 

# Helper function to verify token
def verify_jwt(token):
    try:
        # Get public key from Auth0
        jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)

        # Choose matching key
        rsa_key = {}
        for key in jwks['keys']:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }
        if not rsa_key:
            raise ValueError('No matching RSA key found.')

        # Decode token
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_IDENTIFIER,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )
        return payload
    except Exception as e:
        raise ValueError(f"Token verification failed: {str(e)}")

# Route to handle user requests will be /user_data

def get_user_data():
    auth_header = request.headers.get('Authorization', None)
    if not auth_header:
        return jsonify({"message": "Authorization header is missing"}), 401

    try:
        token = auth_header.split()[1]
        payload = verify_jwt(token)

        # Use payload to identify the user and fetch data
        user_id = payload['sub']  # Typically "auth0|<user_id>"
        # Query your database here using user_id
        user_data = {"id": user_id}  # Replace with actual DB query

        return jsonify(user_data)
    except ValueError as e:
        return jsonify({"message": str(e)}), 401