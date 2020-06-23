from flask import make_response
from flask.json import jsonify

def respond(data, code=200, content_type='application/json'):
	
	resp = make_response(jsonify(data), code)
	resp.headers['Content-Type'] = content_type
	return resp


def make_response_data(message, list_id):
	# TODO: maybe make this into an object at some point
	return {
		"message": message,
		"list-id": list_id
	}
