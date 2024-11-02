from flask_socketio import emit
from flask import session

from .models import Message
from .extension import socketio

# @socketio.on("message")
# def sendMessage(message):
#     print("sent")
#     send(message, broadcast=True)


@socketio.on('message')
def text(message):    
    message = Message( text=text)
    db.session.add(message)
    db.session.commit()
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']})