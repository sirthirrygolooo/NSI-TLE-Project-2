from flask import Blueprint,request
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

def get_infos():
	name = request.form.getlist('name')
	fname = request.form.getlist('fname')

	return name,fname

data = []

@main.route('/')
def presentation():
	
	return render_template("presentation.html")

@main.route('/about')
def about():
	
	return render_template("about.html")

@main.route('/login', methods=['GET', 'POST'])
def login():
	name,fname = get_infos()
	logged_in = False

	if name != [] and fname != []:
		data.append(name)
		data.append(fname)
		logged_in = True
		
	return render_template("login.html")

@main.route('/dashboard')
def dashboard():
	
	return ('This is the dashboard')

@main.route('/test')
def test(datas):
	return render_template("test.html", posts=datas)
