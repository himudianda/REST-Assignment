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
    version = db.Column(db.Integer, server_default='1')
    topic = db.Column(db.Enum(*TOPICS.keys(), name='topic_tags'),
                      index=True, nullable=False, server_default='tech')
    text = db.Column(db.String(255), index=True, nullable=False,
                     server_default='')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',
                                                  onupdate='CASCADE',
                                                  ondelete='CASCADE'),
                        index=True, nullable=False)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Comment, self).__init__(**kwargs)

    def serialize(self, lite=False):
        """
        Return JSON fields to render the comment.

        :return: dict
        """
        from server.blueprints.user.models import User
        user = User.query.get(self.user_id)
        username = user.username if user else ""
        params = {
            'id': self.id,
            'version': self.version,
            'topic': self.topic,
            'text': self.text,
            'created_by': username
        }
        if lite:
            del params['created_by']

        return params

    @classmethod
    def find(cls, _id=None, username=None, topic=None):
        """
        Find comments.

        :param id: Comment id to find
        :type id: str
        :param username: Username of person who created comment
        :type username: str
        :param topic: Comment topic to find
        :type topic: str
        :return: Comments
        """
        comments = Comment.query
        if not topic and not id and not username:
            return comments.all()
        if _id:
            return [comments.get(_id)]

        if topic:
            formatted_topic = topic.lower()
            comments = comments.filter(Comment.topic == formatted_topic)
        if username:
            from server.blueprints.user.models import User
            user = User.query.filter(User.username == username).first()
            if user:
                comments = comments.filter(Comment.user_id == user.id)
        return comments
