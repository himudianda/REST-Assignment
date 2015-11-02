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
        if comments:
            return {'comments': [_c.serialize for _c in comments]}, 200
        else:
            abort(404)

    # curl -i -X POST -H "Content-Type: application/json" -d '{"topic":"health", "text": "A glass of Red wine isnt that bad"}' http://localhost:8000/comments
    def post(self):
        args = self.reqparse.parse_args()
        comment = Comment(topic=args['topic'], text=args['text'])
        comment.save()
        return {'comment': comment.serialize}, 201


class CommentAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('topic', type=str, location='json')
        self.reqparse.add_argument('text', type=str, location='json')
        super(CommentAPI, self).__init__()

    # curl -i -X GET http://localhost:8000/comment/1
    def get(self, id):
        comment = Comment.query.get(id)
        if comment:
            return {'comment': comment.serialize}, 200
        else:
            abort(404)

    # curl -i -X PUT -H "Content-Type: application/json" -d '{"topic":"entertainment", "text": "Steve jobs movie opened with a 2 star rating."}' http://localhost:8000/comment/4
    def put(self, id):
        comment = Comment.query.get(id)
        if comment:
            args = self.reqparse.parse_args()
            comment.topic = args['topic']
            comment.text = args['text']
            comment.save()
            return {'comment': comment.serialize}, 200
        else:
            abort(404)

    # curl -i -X DELETE http://localhost:8000/comment/4
    def delete(self, id):
        comment = Comment.query.get(id)
        if comment:
            comment.delete()
            return {'result': True}, 204
        else:
            return {'result': False}, 404


api.add_resource(CommentListAPI, '/comments')
api.add_resource(CommentAPI, '/comment/<int:id>')
