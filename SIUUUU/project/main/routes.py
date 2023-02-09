from flask import Blueprint

main = Blueprint('main', __name__)

from flask import Blueprint, render_template

@main.route('/')
def presentation():
	
	return render_template("presentation.html")

@main.route('/about')
def about():
	
	return render_template("about.html")