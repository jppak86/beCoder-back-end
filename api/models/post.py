from datetime import datetime
from api.models.db import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    code_block = db.Column(db.String(250))
    explanation = db.Column(db.String(250))
    do_good  = db.Column(db.String(250))
    do_bad = db.Column(db.String(250))
    do_next = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
      return f"Post('{self.id}', '{self.title}'"

    def serialize(self):
      post = {c.title: getattr(self, c.title) for c in self.__table__.columns}
      return post