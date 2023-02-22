from flask import Blueprint, jsonify
from blockch import *
from datas import *

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
	return "Hello, World! This is the admin page click <a href='/admin/get_chain'>here</a> to get the chain"

@admin.route('/mine_block', methods=['GET'])
def mine_block():
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
                'vote': block['vote']
                }
 
    return jsonify(response), 200

 
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