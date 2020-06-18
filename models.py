from flask_sqlalchemy import SQLAlchemy
import uuid
from helpers.guid import HashColumn


db = SQLAlchemy()

def get_uuid():
	return uuid.uuid4().hex

class List(db.Model):
	__tablename__ = "lister_lists"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	name = db.Column(db.String(80), unique=True, nullable=False)

	# def __repr__(self):
	# 	return '<List %r>' % self.id
