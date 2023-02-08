from flask import Flask
from project import config
from project.main.routes import main
from project.admin.routes import admin
from project.models import login_manager,db,User,Post

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
app.config.from_object(config.DevelopmentConfig)
with app.app_context():
	login_manager.init_app(app)
    
with app.app_context():
    db.init_app(app)

@app.shell_context_processor
def make_shell_context():
	return {'app': app, 'db': db, 'User': User, 'Post': Post}