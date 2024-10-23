from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import asc
from .models import User, Message
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template('index.html')

@views.route("/message", methods=['GET', 'POST'])
def message():
    if request.method == "POST":
        message = request.form.get('message')
        print(message)
        
    if not message:
        flash('Category Name cannot be empty', category='error')
    else:
            msg = Message(text = message, author=current_user.id)
            db.session.add(msg)
            db.session.commit()
            flash('Text sent!', category='success')
    return redirect(url_for("views.home"))