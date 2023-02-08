from flask import Blueprint

main = Blueprint('main', __name__)

from flask import Blueprint, render_template

@main.route('/')
def home():
	posts = [
		{
			"body": "Hello, this is a post",
			"timestamp": "This is a date and time",
		}
	]
	
	return render_template("home.html", posts=posts)

@main.route('/parallax')
def parallax():
	return render_template("parallax.html")