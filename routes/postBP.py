from flask import Blueprint
from controllers.postController import create_post, get_post_by_id, get_all_posts, get_posts_by_neighbor_id, get_posts_by_zipcode, update_post, delete_post

post_blueprint = Blueprint('post_bp', __name__)

#url_prefix='/post'

post_blueprint.route('/', methods=['POST'])(create_post)
post_blueprint.route('/', methods=['GET'])(get_all_posts)
post_blueprint.route('/<post_id>', methods=['GET'])(get_post_by_id)
post_blueprint.route('/neighbor/<neighbor_id>', methods=['GET'])(get_posts_by_neighbor_id)
post_blueprint.route('/zipcode/<zipcode>', methods=['GET'])(get_posts_by_zipcode)
post_blueprint.route('/<post_id>', methods=['PUT'])(update_post)
post_blueprint.route('/<post_id>', methods=['DELETE'])(delete_post)
