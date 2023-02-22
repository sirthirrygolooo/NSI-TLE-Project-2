import datetime,hashlib,json
from datas import *

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')


    # Création d'un bloc avec ses différentes infos (position, horodatage, vote, hash précédent, etc...) 
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'vote' : str(candidats[0]['candidat']),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    # pour récupérer le hash du bloc précédent
    def print_previous_block(self):
        return self.chain[-1]
 
    # Obtient la preuve d'un bloc
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
 
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
 
        return new_proof
 
    # Hash un bloc en renvoie la valeur (sha-256)
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
 
    # Verifie la validité de la chaine en sa basant sur le hash du bloc précédent 
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
 
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
 
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
 
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
 
        return True