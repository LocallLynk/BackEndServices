from flask import Flask, render_template
from flask_socketio import SocketIO





app = Flask(__name__)

message_storage = []
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin = '*')# set cors to allow all origins with *

userlog = {}

@socketio.on('connect') #this wrapper is responsible for triggering the following function based on the specified event
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client Disconnected')

@socketio.on('message')#when a message comes through, create an empty list that gets appended
def handle_message(message): # When listening for a message events, takes in a message as an argument
    print(f"Message: {message}")
    user = message.split()[0].strip(':')
    if user in userlog:
        userlog[user].append(message)
    else:
        userlog[user]= [message]
    print(userlog)
    socketio.emit('message', message) #.emit() method broadcasts a special message to everyone connected
   


@app.route('/chat')
def home():
    return render_template('input html file where user can input their name and message')


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)


""" In the chat.py file, we have a Flask app that uses the Flask-SocketIO extension 
 to enable real-time communication between the server and clients. The app has a 
 message storage list to store messages and a userlog dictionary to store messages by user. 
 The app has a route for the home page that renders an input HTML file where users 
 can input their name and message. The app listens for message events and emits 
 messages to all connected clients. The app runs the SocketIO server when executed."""



