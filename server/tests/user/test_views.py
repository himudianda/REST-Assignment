from flask import url_for

from server.tests.lib.util import ViewTestMixin
from server.tests.lib.assertions import assert_status_with_message
from server.blueprints.user.models import User


class TestUser(ViewTestMixin):

    def test_get_users(self):
        response = self.client.get('http://localhost:8000/users', headers=self.headers)
        assert response.status_code == 200
