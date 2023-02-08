# Simple BlockChain in Python

import hashlib
import datetime
import json
from flask import Flask, jsonify

# Creating a Blockchain

class Blockchain:


    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    # Creating a block in the Blockchain

    def create_block(self, proof, previous_hash):

        block = {'index': len(self.chain) + 1,

        'timestamp': str(datetime.datetime.now()),
        'proof': proof,
        'previous_hash': previous_hash}










        


