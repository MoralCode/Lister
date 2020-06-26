from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from helpers.guid import HashColumn
from helpers.helpers import get_uuid

db = SQLAlchemy()

table_prefix = os.getenv("LISTER_TABLE_PREFIX", "lister_")

class List(db.Model):
	__tablename__ = table_prefix+"lists"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	name = db.Column(db.String(80), nullable=False)
	description = db.Column(db.String(1024), nullable=True)

	# def __repr__(self):
	# 	return '<List %r>' % self.id

class Person(db.Model):
	__tablename__ = table_prefix+"people"
	id = db.Column(HashColumn(length=32),
						primary_key=True, default=get_uuid)
	# https://stackoverflow.com/a/7717596/
	email = db.Column(db.String(254), unique=True, nullable=False)
	# black magic: https://docs.sqlalchemy.org/en/13/orm/join_conditions.html#specifying-alternate-join-conditions
	# https://stackoverflow.com/a/37445153
	# lists = db.relationship(
	# 	List,
	# 	# https://stackoverflow.com/a/19261449
	# 	secondary="lister_subscriptions",#lambda:Subscription.__tablename__,
	# 	backref="members",
	# 	primaryjoin="and_(Person.id==Subscription.person_id, "
    #                     "Subscription.token.is_(None))",
	# 	secondaryjoin="and_(List.id==Subscription.list_id, "
    #                     "Subscription.token.is_(None))"
	# )

	# def __repr__(self):
	# 	return '<List %r>' % self.id

class Subscription(db.Model):
	__tablename__ = table_prefix+'subscriptions'
	list_id = db.Column(HashColumn(length=32), db.ForeignKey(List.id), primary_key=True)
	person_id = db.Column(HashColumn(length=32), db.ForeignKey(Person.id), primary_key=True)
	token = db.Column(HashColumn(length=32), default=get_uuid)
	date_subscribed = db.Column(db.DateTime, default=datetime.utcnow())

	person = db.relationship(Person, backref="subscriptions")
	list = db.relationship(List, backref="subscriptions")
