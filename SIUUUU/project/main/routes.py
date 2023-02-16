from flask import Blueprint,request, render_template, redirect, url_for
from project.main.datas import get_candidats,candidats


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
	name,fname = [],[]
	name,fname = get_infos()

	if name != [] and fname != []:
		data.append(name)
		data.append(fname)
		return redirect(url_for("main.dashboard", name=name[0], fname=fname[0]))
		
	return render_template("login.html")

@main.route('/dashboard/<string:name>-<string:fname>')
def dashboard(name, fname):
	# return (f'This is the dashboard of {data[1]} {data[0]}',print(data[0]))
	get_cand = get_candidats(candidats)
	return render_template("index.html", posts=data, candidats=get_cand,name=name,fname=fname)

@main.route('/test')
def test(datas):
	return render_template("test.html", posts=datas)
