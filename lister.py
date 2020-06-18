from flask import Flask, render_template
import logging
from models import db

app_logger = logging.getLogger('lister')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
db.init_app(app)

@app.route("/")
def index():
	return render_template("index.html")


if __name__ == "__main__":
	app.run()