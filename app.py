from flask import Flask, render_template, request
from flask_socketio import SocketIO
from database import db
from models.schema import ma
from routes.feedbackBP import feedback_blueprint
from routes.neighborBP import neighbor_blueprint
from routes.skillBP import skill_blueprint
from routes.taskBP import task_blueprint
from routes.postBP import post_blueprint
from routes.commentBP import comment_blueprint
from routes.likeBP import like_blueprint
from routes.dislikeBP import dislike_blueprint
from routes.shareBP import share_blueprint
from limiter import limiter
from flask_cors import CORS
from cache import cache
from flask_swagger_ui import get_swaggerui_blueprint
from chat import app as chat_app
from services.SkillService import populate_skill_bank
import jwt

SWAGGER_URL = '/api/docs' # URL endpoint to view our docs
API_URL = '/static/swagger.yaml'#Grabs our host from our swagger.yaml file

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'LocalLynk'})

def create_app(config_name):
    app = Flask(__name__) # instantiate the Flask app

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    blueprint_config(app)
    rate_limit_config(app)
    cache.init_app(app)
    CORS(app)
    socketio = SocketIO(app)
    socketio.init_app(app)
    



    return app


def blueprint_config(app):
    app.register_blueprint(feedback_blueprint, url_prefix='/feedback')
    app.register_blueprint(neighbor_blueprint, url_prefix='/neighbor')
    app.register_blueprint(skill_blueprint, url_prefix='/skill')
    app.register_blueprint(task_blueprint, url_prefix='/task')
    app.register_blueprint(post_blueprint, url_prefix='/post')
    app.register_blueprint(comment_blueprint, url_prefix='/comment')
    app.register_blueprint(like_blueprint, url_prefix='/like')
    app.register_blueprint(dislike_blueprint, url_prefix='/dislike')
    app.register_blueprint(share_blueprint, url_prefix='/share')
    # app.register_blueprint(chat_app, url_prefix='/chat')
    app.register_blueprint(swagger_blueprint, url_prefux=SWAGGER_URL)


def rate_limit_config(app):
    limiter.init_app(app)
    limiter.limit('150 per hour')(feedback_blueprint)
    limiter.limit('150 per hour')(neighbor_blueprint)
    limiter.limit('150 per hour')(skill_blueprint)
    limiter.limit('150 per hour')(task_blueprint)
    limiter.limit('150 per hour')(swagger_blueprint)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    with app.app_context():
        db.create_all()
        populate_skill_bank(db.session)
    app.run()

#implement the inability to type special characters in the input fields