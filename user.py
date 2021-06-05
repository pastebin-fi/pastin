from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from main import db, login_manager

class User(UserMixin, db.Model):
    username = db.Column(db.String(32), primary_key=True, unique=True)
    # RFC 5321, an errata against RFC 3696, states that the maximum length of
    # an email address is 254.
    email = db.Column(db.String(254), unique=True)
    pwd = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def set_password(self, pwd):
        self.pwd = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.pwd, pwd)

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
