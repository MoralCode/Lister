from flask import Blueprint, render_template

blueprint = Blueprint('admin', __name__)


@blueprint.route("/")
def index():
	return render_template("web/admin.html")