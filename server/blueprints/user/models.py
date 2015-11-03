from server.extensions import db


class User(db.Model):
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