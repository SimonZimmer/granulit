from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(3000))
    releases = db.Column(db.String(30000))
    podcasts = db.Column(db.String(30000))
    videos = db.Column(db.String(30000))
    contact = db.Column(db.String(5000))
    impressum = db.Column(db.String(500000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __iter__(self):
        yield "content", {'bio': self.bio, 
                          'releases': self.releases,
                          'podcasts': self.podcasts,
                          'videos': self.videos,
                          'contact': self.contact,
                          'impressum': self.impressum}

    def latest(self):
        try:
            all_text = self.query.all()[-1]
            return all_text
        except:
            pass

        return {}

    def __repr__(self):
        return '<Content {}>'.format(self.id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

