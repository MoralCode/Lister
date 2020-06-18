from flask import Flask
import logging

app_logger = logging.getLogger('lister')

app = Flask(__name__)


@app.route("/")
def index():
    return "Hi"


if __name__ == "__main__":
    app.run()