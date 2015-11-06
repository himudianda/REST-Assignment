import pytest


class ViewTestMixin(object):

    @pytest.fixture(autouse=True)
    def set_common_fixtures(self, client):
        self.client = client
