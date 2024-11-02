from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from sqlalchemy import asc
from .models import User, Message
from . import db
from flask_socketio import emit
from .extension import socketio

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    msg = Message.query.order_by(asc(Message.date_created)).all()
    user = User.query.all()
    return render_template("index.html", users=current_user, msg=msg, user=user)

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




@socketio.on('message')
def text(message):    
    message = Message( text=text)
    db.session.add(message)
    db.session.commit()
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']})