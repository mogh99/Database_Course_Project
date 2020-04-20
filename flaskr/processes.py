"""
	This file process all the froms responses
	for the admin, and the guest users. 
"""
from flask import Blueprint
processesApp = Blueprint('test', __name__, url_prefix="/processes")


@processesApp.route("/test")
def test():
	return "HELLO WORLD"
