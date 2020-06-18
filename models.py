from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime
from helpers.guid import HashColumn


db = SQLAlchemy()

def get_uuid():
	return uuid.uuid4().hex

class Subscription(db.Model):
	__tablename__ = 'lister_subscriptions'
	list_id = db.Column(HashColumn(length=32), db.ForeignKey(List.id), primary_key=True)
	person_id = db.Column(HashColumn(length=32), db.ForeignKey(Person.id), primary_key=True)
	token = db.Column(HashColumn(length=32), default=get_uuid)
	date_subscribed = db.Column(db.DateTime, default=datetime.utcnow())


class List(db.Model):
	__tablename__ = "lister_lists"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	name = db.Column(db.String(80), unique=True, nullable=False)
	members = db.relationship(
		Person,
		secondary=Subscription,
		backref="lists")

	# def __repr__(self):
	# 	return '<List %r>' % self.id

class Person(db.Model):
	__tablename__ = "lister_people"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	# https://stackoverflow.com/a/7717596/
	email = db.Column(db.String(254), unique=True, nullable=False)

	# def __repr__(self):
	# 	return '<List %r>' % self.id
