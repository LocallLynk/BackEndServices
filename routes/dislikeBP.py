from flask import Blueprint
from controllers.dislikeController import add_dislike, remove_dislike

dislike_blueprint = Blueprint('dislike_bp', __name__)

#url_prefix='/dislike'

dislike_blueprint.route('/', methods=['POST'])(add_dislike)
dislike_blueprint.route('/<dislike_id>', methods=['DELETE'])(remove_dislike)