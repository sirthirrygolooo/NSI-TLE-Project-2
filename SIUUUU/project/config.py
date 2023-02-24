import os

BASE_DIR = os.path.abspath(os.path.dirname(__name__))

class BaseConfig(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcdef123456'
	DEBUG = False
	TESTING = False
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
	# SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	TESTING = True

class TestingConfig:
	DEBUG = False
	TESTING = True