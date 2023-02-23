from flask import Blueprint,request, render_template, redirect, url_for,jsonify
from datas import *
from blockch import *

main = Blueprint('main', __name__)
voteu = []

def get_infos():
	name = request.form.getlist('name')
	fname = request.form.getlist('fname')

	return name,fname

data = []
vote = []

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
	# return (f'Dashboard de {data[1]} {data[0]}',print(data[0]))
	get_cand = get_candidats(candidats)
	get_st = get_stats(candidats)
	return render_template("index.html", posts=data, candidats=get_cand,name=name,fname=fname,stats=get_st)

@main.route('/vote', methods=['GET', 'POST'])
def vote():
	vote = []
	vote = request.form.getlist('vote')

	get_cand = get_candidats(candidats)

	if vote != [] :
		# return(f'Vous avez voté {get_candidats(candidats)[int(vote[0])]["candidat"]}')
		voted = True
		voteu.append(get_candidats(candidats)[int(vote[0])]["candidat"])
		return redirect(url_for("main.mine_block", has_voted=voted,vote=get_candidats(candidats)[int(vote[0])]["candidat"]))

	return render_template("vote.html", candidats=get_cand)

@main.route('/vote/<string:has_voted>/<string:vote>')
def mine_block(has_voted,vote):
	if has_voted == 'True':
		previous_block = blockchain.print_previous_block()
		previous_proof = previous_block['proof']
		proof = blockchain.proof_of_work(previous_proof)
		previous_hash = blockchain.hash(previous_block)
		block = blockchain.create_block(proof, previous_hash)
	
		response = {'message': 'Minage nouveau bloc',
					'index': block['index'],
					'timestamp': block['timestamp'],
					'proof': block['proof'],
					'previous_hash': block['previous_hash'],
					# 'vote': block['vote']
					'vote' : vote,
					}

		raw = jsonify(response)
		return render_template('voted.html', raws=response, vote=vote, name=data[1][0], fname=data[0][0])
	else :
		return redirect(url_for("main.vote"))

@main.route('/test')
def test(datas):
	return render_template("test.html", posts=datas)

blockchain = Blockchain()