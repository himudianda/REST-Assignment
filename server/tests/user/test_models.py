from server.blueprints.user.models import User


class TestUser(object):

    def test_serialize_users(self, test_data):
        users = User.query.all()
        for user in users:
            _user = user.serialize()
            assert _user.get('id') == user.id
            assert _user.get('username') == user.username

            # Test that comments have been serialized correctly
            for comment, _comment in zip(user.comments, _user.get('comments')):
                assert _comment.get('id') == comment.id
                assert _comment.get('version') == comment.version
                assert _comment.get('topic') == comment.topic
                assert _comment.get('text') == comment.text
                assert _comment.get('created_by', None) is None
