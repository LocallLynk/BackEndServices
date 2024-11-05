from flask import Flask, render_template
from flask_socketio import SocketIO
from database import db
from models.neighbor import Neighbor
from models.skill import Skill
from models.task import Task
from models.feedback import Feedback
from models.schemas import ma
from routes.feedbackBP import feedback_blueprint
from routes.neighborBP import neighbor_blueprint
from routes.skillBP import skill_blueprint
from routes.taskBP import task_blueprint
from limiter import limiter
from flask_cors import CORS
from cache import cache
from flask_swagger_ui import get_swaggerui_blueprint
SWAGGER_URL = '/api/docs' # URL endpoint to view our docs
API_URL = '/static/swagger.yaml'#Grabs our host from our swagger.yaml file

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'LocalLynk'})

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
   


@app.route('/')
def home():
    return render_template('base.html')


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)