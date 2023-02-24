from project import app

try :
	import flask
	print('flask ok')
	import hashlib
	print('hashlib ok')
except ImportError:
	print('Libs non installées')
	print('Installation des libs...')
	import os
	os.system('pip install requirements.txt')
	os.system('pause')



if __name__=='__main__':
	app.run(host='127.0.0.1',port=5000)