from flask_sqlalchemy import SQLAlchemy
import uuid, os
from datetime import datetime
from helpers.guid import HashColumn


db = SQLAlchemy()

table_prefix = os.getenv("LISTER_TABLE_PREFIX", "lister_")

def get_uuid():
	return uuid.uuid4().hex

class List(db.Model):
	__tablename__ = table_prefix+"lists"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	name = db.Column(db.String(80), unique=True, nullable=False)
	description = db.Column(db.String(1024), unique=True, nullable=True)

	# def __repr__(self):
	# 	return '<List %r>' % self.id

class Person(db.Model):
	__tablename__ = table_prefix+"people"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	# https://stackoverflow.com/a/7717596/
	email = db.Column(db.String(254), unique=True, nullable=False)
	lists = db.relationship(
		List,
		secondary="Subscription",
		backref="members")

	# def __repr__(self):
	# 	return '<List %r>' % self.id

class Subscription(db.Model):
	__tablename__ = table_prefix+'subscriptions'
	list_id = db.Column(HashColumn(length=32), db.ForeignKey(List.id), primary_key=True)
	person_id = db.Column(HashColumn(length=32), db.ForeignKey(Person.id), primary_key=True)
	token = db.Column(HashColumn(length=32), default=get_uuid)
	date_subscribed = db.Column(db.DateTime, default=datetime.utcnow())