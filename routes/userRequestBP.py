from flask import Blueprint
from utils.util import get_user_data

userData_blueprint = Blueprint('request_bp', __name__)

#url_prefix='/user_data'

userData_blueprint.route('/', methods=['GET'])(get_user_data)

