from flask import Blueprint,request
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def presentation():
	
	return render_template("presentation.html")

@main.route('/about')
def about():
	
	return render_template("about.html")

@main.route('/login', methods=['GET', 'POST'])
def login():
	name = request.form.getlist('name')
	fname = request.form.getlist('fname')
	print(f'Nom : {name}\nPrénom: {fname}')

	return render_template("login.html")

@main.route('/home' , methods=['GET', 'POST'])
def home():
	name = request.form.getlist('name')
	fname = request.form.getlist('fname')

	return "name: ",name,"fname: ",fname
