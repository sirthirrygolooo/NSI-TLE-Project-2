from flask import Blueprint,request

main = Blueprint('main', __name__)

from flask import Blueprint, render_template

@main.route('/')
def presentation():
	
	return render_template("presentation.html")

@main.route('/about')
def about():
	
	return render_template("about.html")

@main.route('/login', methods=['GET', 'POST'])
def login():
	data = request.form
	print(data)
	
	return render_template("login.html")