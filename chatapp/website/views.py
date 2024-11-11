from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from sqlalchemy import asc
from .models import User, Message
from . import db
from flask_socketio import send
from .extension import socketio

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    user = User.query.all()
    return render_template("index.html", users=current_user, user=user)

@views.route("/chat/<id>")
@login_required
def chat(id):
    chat_user = User.query.filter_by(id=id).first()
    messages = Message.query.order_by(asc(Message.date_created)).all()
    return render_template("chat.html", messages=messages, chat=chat_user)


@socketio.on("message")
def sendMessage(message):
    
    print("sent")
    
    messages = Message(text = message, author=current_user.id)
    db.session.add(messages)
    db.session.commit()
    
    send(message, broadcast=True)