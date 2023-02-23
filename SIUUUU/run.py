from project import app


try :
	import flask
	import hashlib
except ImportError:
	print('Libs non installées')
	import os
	os.system('pip install requirements.txt')



if __name__=='__main__':
	app.run(host='127.0.0.1',port=5000)