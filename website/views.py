from flask import Blueprint, render_template

views = Blueprint('views', __name__) #dont have to name it like this, __name__ is syntax

@views.route('/') # / stands for home page
def home():
    return render_template("home.html")
