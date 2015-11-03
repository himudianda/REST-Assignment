from server.extensions import db, bcrypt
from server.lib.util_sqlalchemy import ResourceMixin

class User(ResourceMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, index=True)
    password = db.Column(db.String(128), nullable=False, server_default='')


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

    @property
    def serialize(self):
        """
        Return JSON fields to render the user.

        :return: dict
        """
        params = {
            'id': self.id,
            'username': self.username
        }

        return params