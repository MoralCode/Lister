from flask import Flask, render_template, request, make_response
import logging
from models import List, db
import sys
from blueprints import admin
from validate_email import validate_email_or_fail
from validate_email.exceptions import DomainBlacklistedError, EmailValidationError
from flask_cors import CORS
from flask.json import jsonify
from helpers.helpers import make_response_data, respond, get_uuid

app_logger = logging.getLogger('lister')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

CORS(app, origins="*", send_wildcard=True)
app.register_blueprint(admin.blueprint, url_prefix='/admin')

db.init_app(app)

@app.route("/")
def index():
	return render_template("web/index.html")


@app.route("/confirm", methods=['GET'])
def confirm():
	"""
	handles the confirmation action from the link that was in the users confirmation email and return the success page
	"""
	# TODO: get the information from the DB for the confirmation token
	# request.args.get("token")
	# TODO: set token to NULL to indicate that the email was verified and return success page
	return ""

@app.route("/subscribe", methods=['POST'])
def subscribe():
	"""
	receives the form data from the subscription form and triggers the sending of the confirmation email, along with all the database changes that go with it
	"""
	# POST parameters: list ID, or multiple list ID's, email address
	# https://stackoverflow.com/a/28982264

	if request.form.get('email') is None:
		return respond(make_response_data(
							"You must enter an email address",
							request.form.get('listid')
							),
						code=400)


	try:
		validate_email_or_fail(email_address=request.form.get('email'), check_mx=False)
	except EmailValidationError as e:
		err_msg = ""
		if isinstance(e, DomainBlacklistedError):
			err_msg = "Disposable email addresses are not allowed."
		else:
			err_msg = "Invalid Email address. Please try again"

		if request.args.get("redirect"):
			return render_template("web/subscribeform.html", error=err_msg, list_id=request.form.get('listid')) #email=email
		else:
			return respond(
				make_response_data(err_msg, request.form.get('listid')),
				code=400)


	#send confirmation email and add to DB
	if request.args.get("redirect"):
		return render_template("web/subscribesuccess.html")
	else:
		return respond(make_response_data(
					"Check your email to confirm your subscription!",
					request.form.get('listid')
					)
				)

@app.route("/embed", methods=['GET'])
def embed_subscribe():
	"""
	returns an embeddable form suitable for an iFrame.
	accepts the URL parameter listid for the id of the list to subscribe the user to
	"""
	return render_template("web/subscribeform.html", list_id=request.args.get("listid"))


if len(sys.argv) > 1 and sys.argv[1] == "setup":
# https://stackoverflow.com/a/46541219
	with app.app_context():
		db.create_all()
		if db.query(List).first() is None:
			testList = List(name="Test List", description="a sample list for testing purposes")
			db.session.add(testList)
			print(testList.id)
		db.session.commit()
		print("Setup Complete.")
		exit(0)

if __name__ == "__main__":
	app.run()