from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

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

    from .models import User, Note # this import just needs to make sure our models.py file is running, not to actually use its contents

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where the user will go if he/she is not logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #automatically knows to find from primary key

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
