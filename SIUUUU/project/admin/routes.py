from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
	return "Hello, World! This is the admin page."

@admin.route('/secretPage')
def secretPage():
	return "Hello, World! This is the admin secret page."