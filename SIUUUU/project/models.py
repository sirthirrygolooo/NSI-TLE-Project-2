from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()

User = db.Table('user', db.Model.metadata)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(256))

	def __init__(self, body):
		self.body = body

	def __repr__(self):
		return "<Post({})>".format(self.id)


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))