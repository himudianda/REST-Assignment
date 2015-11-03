from flask import Blueprint, abort, request
from flask.ext.restful import Api, Resource, reqparse

from server.blueprints.user.models import User

user = Blueprint('user', __name__)
api = Api(user)

class UserListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username provided',
                                   location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided',
                                   location='json')
        super(UserListAPI, self).__init__()

    # curl -i -X GET http://localhost:8000/users
    def get(self):
        users = User.query.all()
        return {'users': [_u.serialize for _u in users]}, 200

    # curl -i -X POST -H "Content-Type: application/json" -d '{"username":"himudianda", "password": "ab12yz34"}' http://localhost:8000/users
    def post(self):
        args = self.reqparse.parse_args()
        user = User(username=args['username'], password=args['password'])
        user.save()
        return {'user': user.serialize}, 201


class UserAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserAPI, self).__init__()

    # curl -i -X GET http://localhost:8000/user/1
    def get(self, id):
        user = User.query.get(id)
        if user:
            return {'user': user.serialize}, 200
        else:
            abort(404)

    # curl -i -X PUT -H "Content-Type: application/json" -d '{"username":"imudiand", "password": "ab12yz34"}' http://localhost:8000/user/4
    def put(self, id):
        user = User.query.get(id)
        if user:
            args = self.reqparse.parse_args()
            user.username = args['username']
            user.password = args['password']
            user.save()
            return {'user': user.serialize}, 200
        else:
            abort(404)

    # curl -i -X DELETE http://localhost:8000/user/4
    def delete(self, id):
        user = User.query.get(id)
        if user:
            user.delete()
            return {'result': True}, 204
        else:
            return {'result': False}, 404


api.add_resource(UserListAPI, '/users')
api.add_resource(UserAPI, '/user/<int:id>')
