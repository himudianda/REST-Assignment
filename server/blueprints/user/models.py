from server.extensions import db, bcrypt
from server.lib.util_sqlalchemy import ResourceMixin
from server.blueprints.comment.models import Comment


class User(ResourceMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False, server_default='')
    comments = db.relationship(Comment, backref='users', passive_deletes=True)


    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(User, self).__init__(**kwargs)
        self.password = User.encrypt_password(kwargs.get('password', ''))

    @classmethod
    def encrypt_password(cls, plaintext_password):
        """
        Hash a plaintext string using bcrypt.

        :param plaintext_password: Password in plain text
        :type plaintext_password: str
        :return: str
        """
        if plaintext_password:
            return bcrypt.generate_password_hash(plaintext_password, 8)

        return None

    def serialize(self):
        """
        Return JSON fields to render the user.

        :return: dict
        """
        params = {
            'id': self.id,
            'username': self.username,
            'comments': [ _c.serialize(lite=True) for _c in Comment.query.filter(Comment.user_id == self.id) ]
        }

        return params