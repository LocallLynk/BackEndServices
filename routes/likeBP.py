from flask import Blueprint
from controllers.likeController import add_like, remove_like

like_blueprint = Blueprint('like_bp', __name__)

#url_prefix='/like'

like_blueprint.route('/add', methods=['POST'])(add_like)
like_blueprint.route('/delete/<like_id>', methods=['DELETE'])(remove_like)