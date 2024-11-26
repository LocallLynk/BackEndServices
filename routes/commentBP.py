from flask import Blueprint
from controllers.commentController import add_comment, get_all_comments, get_comment_by_id, update_comment, delete_comment, get_comments_by_post_id, get_comments_by_neighbor_id

comment_blueprint = Blueprint('comment_bp', __name__)

#url_prefix='/comment'

comment_blueprint.route('/add', methods=['POST'])(add_comment)
comment_blueprint.route('/get', methods=['GET'])(get_all_comments)
comment_blueprint.route('/get/<comment_id>', methods=['GET'])(get_comment_by_id)
comment_blueprint.route('/get/post/<post_id>', methods=['GET'])(get_comments_by_post_id)
comment_blueprint.route('/get/neighbor/<neighbor_id>', methods=['GET'])(get_comments_by_neighbor_id)
comment_blueprint.route('/update/<comment_id>', methods=['PUT'])(update_comment)
comment_blueprint.route('/delete/<comment_id>', methods=['DELETE'])(delete_comment)