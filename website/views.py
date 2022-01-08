from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user #current_user can only be used if we use UserMixin in moddels.py
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #dont have to name it like this, __name__ is syntax

@views.route('/', methods=['GET', 'POST']) # / stands for home page
@login_required
def home():
    if request.method =='POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category = 'error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId'] #json creates a dictionary that includes our noteID and its data
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({}) #empty response to show success or error; flask requires to return something
