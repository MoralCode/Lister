from flask import Flask, render_template
import logging
from models import db
import sys

app_logger = logging.getLogger('lister')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
db.init_app(app)

@app.route("/")
def index():
	return render_template("index.html")



if sys.argv[1] == "setup":
# https://stackoverflow.com/a/46541219
    with app.app_context():
        db.create_all()
        db.session.commit()
        print("Setup Complete.")
        exit(0)

if __name__ == "__main__":
	app.run()