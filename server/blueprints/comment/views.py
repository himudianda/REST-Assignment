from flask import Blueprint, abort
from flask.ext.restful import Api, Resource, reqparse

from server.blueprints.comment.models import Comment

comment = Blueprint('comment', __name__)
api = Api(comment)

comments = [
    {
        'id': 1,
        'topic': u'Science & Technology',
        'text': u'Microsoft hololens could go '
                 'into production beginning next year.'
    },
    {
        'id': 2,
        'topic': u'Politics',
        'text': u'Is Jeb Bush losing the republican primary ?'
    }
]


class CommentListAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('topic', type=str, required=True,
                                   help='No comment topic provided',
                                   location='json')
        self.reqparse.add_argument('text', type=str, default="",
                                   location='json')
        super(CommentListAPI, self).__init__()


    # curl -i -X GET http://localhost:8000/comments
    def get(self):
        comments = Comment.query.all()
        return {'comments': [ _c.serialize for _c in comments ]}, 200


    # curl -i -X POST -H "Content-Type: application/json" -d '{"topic":"health", "text": "A glass of Red wine isnt that bad"}' http://localhost:8000/comments
    def post(self):
        args = self.reqparse.parse_args()
        comment = {
            'id': comments[-1]['id'] + 1,
            'topic': args['topic'],
            'text': args['text']
        }
        comments.append(comment)
        return {'comment': comment}, 201


class CommentAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('topic', type=str, location='json')
        self.reqparse.add_argument('text', type=str, location='json')
        super(CommentAPI, self).__init__()

    # curl -i -X GET http://localhost:8000/comment/1
    def get(self, id):
        comment = [comment for comment in comments if comment['id'] == id]
        if len(comment) == 0:
            abort(404)
        return {'comment': comment}

    # curl -i -X PUT -H "Content-Type: application/json" -d '{"topic":"entertainment", "text": "Steve jobs movie opened with a 2 star rating."}' http://localhost:8000/comment/4
    def put(self, id):
        comment = [comment for comment in comments if comment['id'] == id]
        if len(comment) == 0:
            abort(404)
        comment = comment[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                comment[k] = v
        return {'comment': comment}

    # curl -i -X DELETE http://localhost:8000/comment/4
    def delete(self, id):
        comment = [comment for comment in comments if comment['id'] == id]
        if len(comment) == 0:
            abort(404)
        comments.remove(comment[0])
        return {'result': True}


api.add_resource(CommentListAPI, '/comments')
api.add_resource(CommentAPI, '/comment/<int:id>')
