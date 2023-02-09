from flask import Blueprint,request

main = Blueprint('main', __name__)

from flask import Blueprint, render_template

@main.route('/')
def presentation():
	
	return render_template("presentation.html")

@main.route('/about')
def about():
	
	return render_template("about.html")

@main.route('/login')
def login():
	
	return render_template("login.html")

@main.route('/sqr', methods=['GET'])
def getSqr():
	num1 = str(request.args.get('num1'))
    
	return f"Square of {num1} is {num1}"