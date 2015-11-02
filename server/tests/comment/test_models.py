import datetime
import pytz

from server.blueprints.comment.models import Comment


class TestComment(object):
    def test_serialize(self):
        params = {
            'id': 1,
            'topic': "health",
            'text': "Random Health Doc"
        }
        comment = Comment(**params)
        _comment = comment.serialize
        assert comment.id == _comment.get('id')
        assert comment.topic == _comment.get("topic")
        assert comment.text == _comment.get("text")
