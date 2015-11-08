import pytest
from base64 import b64encode


class ViewTestMixin(object):

    @pytest.fixture(autouse=True)
    def set_common_fixtures(self, client):
        self.client = client

    @pytest.fixture(autouse=True)
    def set_auth_headers(self, client):
        self.headers = {
            'Authorization': 'Basic ' + b64encode("{0}:{1}".format("admin", "password"))
        }
