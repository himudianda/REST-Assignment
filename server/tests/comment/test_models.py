from server.blueprints.comment.models import Comment
from server.blueprints.user.models import User


class TestComment(object):
    def test_serialize_comments(self, test_data):
        comments = Comment.query.all()
        for comment in comments:
            _comment = comment.serialize()
            assert _comment.get('id') == comment.id
            assert _comment.get('version') == comment.version
            assert _comment.get('topic') == comment.topic
            assert _comment.get('text') == comment.text

            user = User.query.filter(User.username == _comment.get('created_by')).first()
            assert user.id == comment.user_id
