from flask import Blueprint
from controllers.shareController import add_share, remove_share, get_share_by_id, update_share

share_blueprint = Blueprint('share_bp', __name__)

#url_prefix='/share'

share_blueprint.route('/', methods=['POST'])(add_share)
share_blueprint.route('/<share_id>', methods=['GET'])(get_share_by_id)
share_blueprint.route('/<share_id>', methods=['PUT'])(update_share)
share_blueprint.route('/<share_id>', methods=['DELETE'])(remove_share)