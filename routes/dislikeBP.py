from flask import Blueprint
from controllers.dislikeController import add_dislike, remove_dislike

dislike_blueprint = Blueprint('dislike_bp', __name__)

#url_prefix='/dislike'

dislike_blueprint.route('/add', methods=['POST'])(add_dislike)
dislike_blueprint.route('/remove/<dislike_id>', methods=['DELETE'])(remove_dislike)