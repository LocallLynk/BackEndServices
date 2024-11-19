from flask import Blueprint
from controllers.commentController import add_comment, get_all_comments, get_comment_by_id, update_comment, delete_comment, get_comments_by_post_id, get_comments_by_neighbor_id

comment_blueprint = Blueprint('comment_bp', __name__)

#url_prefix='/comment'

comment_blueprint.route('/', methods=['POST'])(add_comment)
comment_blueprint.route('/', methods=['GET'])(get_all_comments)
comment_blueprint.route('/<comment_id>', methods=['GET'])(get_comment_by_id)
comment_blueprint.route('/post/<post_id>', methods=['GET'])(get_comments_by_post_id)
comment_blueprint.route('/neighbor/<neighbor_id>', methods=['GET'])(get_comments_by_neighbor_id)
comment_blueprint.route('/<comment_id>', methods=['PUT'])(update_comment)
comment_blueprint.route('/<comment_id>', methods=['DELETE'])(delete_comment)