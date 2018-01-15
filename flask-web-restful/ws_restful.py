# coding=utf-8
from flask import current_app, Blueprint, jsonify, session, make_response, request
from flask_restful import Resource, Api, fields, marshal_with, reqparse

import json, datetime
from functools import wraps
from mysql_db import mysql

from rx import Observable
import requests
import jwt

# import requests_cache

from flask_restful_swagger_2 import Api, swagger, Schema

ws_restful = Blueprint('ws_restful', __name__)
# api = Api(ws_specialist)
api = Api(
    ws_restful,
    api_version='0.1',
    base_path='/ws-restful',
    api_spec_url='/api/spec',
    produces=['application/json'],
    description='ws-restful Blueprint doc')


# check user token whether valid
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = request.args.get('at')

        if token is not None and token != '':

            try:
                # 进行token过期认证
                user = jwt.decode(token, 0, verify=True)

                return f(*args, **kwargs)

            except jwt.InvalidTokenError:
                return {'result': 250, 'data': None, 'desc': 'token error'}

        else:
            return {'result': 250, 'data': None, 'desc': 'no token'}

    return decorated_function

class CreateToken(Resource):
    """create jwt token"""

    def post(self, uid, name):
        times = datetime.datetime.utcnow() + datetime.timedelta(seconds=36000)

        token = jwt.encode(
            {
                'exp': times,
                'uid': uid,
                'name': name
            },
            'token',
            headers={
                'kid': 'hnyf'
            })

        str_token = str(token, encoding="utf-8")

        if str_token:
            return {'token': str_token, 'result': 0}
        else:
            return {'token': None, 'result': 250}

api.add_resource(CreateToken, '/token/<int:uid>/<string:name>')

#------------------------------json and mysql-------------------------------------
login_parser = reqparse.RequestParser()
login_parser.add_argument(
    'email',
    dest='email',
    type=str,
    location='json',
    required=True,
    help='user email(str) required')
login_parser.add_argument(
    'password', dest='password', type=str, location='json', help='password(str)')

class Login(Resource):
    """user login"""

    def post(self):

        # get json value
        args = login_parser.parse_args()
        email = args['email']
        password = args['password']

        cursor = mysql.connection.cursor()

        sql = 'select * from user where email = "%s" and password = "%s"' % (email, password)

        cursor.execute(sql)

        data = cursor.fetchone()

        if data:
            times = datetime.datetime.utcnow() + datetime.timedelta(seconds=36000)

            token = jwt.encode(
                {
                    'exp': times,
                    'email': email,
                    'id': data['id']
                },
                'token',
                headers={
                    'kid': 'hnyf'
                })

            str_token = str(token, encoding="utf-8")

        if str_token:
            return {'token': str_token, 'result': 0}
        else:
            return {'token': None, 'result': 250}

api.add_resource(Login, '/login')



