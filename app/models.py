import json
import datetime
from app.exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String, primary_key=True)
    display_name = db.Column(db.String)
    email = db.Column(db.String)
    href = db.Column(db.String)
    uri = db.Column(db.String)

    images = db.Column(db.String)

    access_token = db.Column(db.String)
    refresh_token = db.Column(db.String)
    expires = db.Column(db.DateTime)
    scope = db.Column(db.String)
    token_type = db.Column(db.String)

    def to_dict(self) -> dict:
        return self.to_dict_public()

    def to_dict_public(self) -> dict:
        return {
            'display_name': self.display_name,
            'href': self.href,
            'uri': self.uri,
            'images': json.loads(self.images),
            'access_token': self.access_token
        }

    def to_dict_private(self) -> dict:
        d = self.to_dict_public()
        d.update({
            'id': self.id,
            'refresh_token': self.refresh_token,
            'expires': self.expires,
            'scope': self.scope,
            'token_type': self.token_type
        })

class Queue(db.Model):
    __tablename__ = 'queue'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    track_uri = db.Column(db.String)
    date_added = db.Column(db.DateTime, default=datetime.datetime.now)
    next_playable = db.Column(db.DateTime, default=datetime.datetime.now)


class VoteToSkip(db.Model):
    __tablename__ = 'voteskip'

    client_id = db.Column(db.String)
    queue_id = db.Column(db.Integer, db.ForeignKey('queue.id'))
