from collections import OrderedDict

from server.lib.util_sqlalchemy import ResourceMixin
from server.extensions import db


class Comment(ResourceMixin, db.Model):
    __tablename__ = 'comments'

    TOPICS = OrderedDict([
        ('tech', 'Science & Technology'),
        ('politics', 'Politics'),
        ('health', 'Health & Food'),
        ('entertainment', 'Movies, Music & more')
    ])

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.Enum(*TOPICS.keys(), name='topic_tags'),
                      index=True, nullable=False, server_default='tech')
    text = db.Column(db.String(255), index=True, nullable=False,
                     server_default='')

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Comment, self).__init__(**kwargs)

    @property
    def serialize(self):
        """
        Return JSON fields to render the comment.

        :return: dict
        """
        params = {
            'id': self.id,
            'topic': self.topic,
            'text': self.text,
        }

        return params

    @classmethod
    def find(cls, id=None, topic=None):
        """
        Find comments.

        :param id: Comment id to find
        :type id: str
        :param topic: Comment topic to find
        :type topic: str
        :return: Comments
        """
        comments = Comment.query
        if not topic and not id:
            return comments.all()

        if topic:
            formatted_topic = topic.lower()
            comments = comments.filter(Comment.topic == formatted_topic)
        if id:
            comments = comments.filter(Comment.id == id)

        return comments
