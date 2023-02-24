from flask import Blueprint, jsonify,render_template
from blockch import *
from datas import *

admin = Blueprint('admin', __name__)

def mine_block(vote):
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash,vote)
 
    response = {'message': 'Minage nouveau bloc',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'vote': vote
                }
 
    return 200, response

@admin.route('/')
def index():
        
	return render_template("/admin/index.html")


 
@admin.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200



 
@admin.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
 
    if valid:
        response = {'message': 'Blockchain valide !'}
    else:
        response = {'message': '/!\\ Blockchain invalide /!\\'}
    return jsonify(response), 200

print()

blockchain = Blockchain()