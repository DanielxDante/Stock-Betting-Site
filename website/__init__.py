from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # __name__ is default documentation: its part of Flask
    app.config['SECRET_KEY'] = 'daniel' #kind of like an encryption key, can be anything, NEVER SHARE THIS
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views #note the variable names
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note # this import just needs to make sure our models.py file is running, not to actually use its contents, so "import .models" is sufficient

    return app
