from flask import url_for
from json import loads

from server.tests.lib.util import ViewTestMixin
from server.tests.lib.assertions import assert_status_with_message
from server.blueprints.user.models import User
from server.blueprints.comment.models import Comment


class TestUser(ViewTestMixin):

    def test_get_users(self):
        response = self.client.get('http://localhost:8000/users', headers=self.headers)
        assert response.status_code == 200

        data = loads(response.data)

        assert len(data.get('users', [])) == 2
        for user in data.get('users'):
            assert user.get('username', None) in ['admin', 'user1']

            comments = user.get('comments', [])
            assert len(comments) == 1

            assert comments[0].get('topic', None) in Comment.TOPICS.keys()
            assert comments[0].get('text', None) == "A fake comment."
            assert comments[0].get('version', None) == 1
