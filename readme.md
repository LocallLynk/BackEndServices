LocalLynk Routes

This is to allow us to check off routes as we test them, so we know what works and what doesn't at a glance!

-mark working routes with an upper-case 'X' in front of the dash

NeighborBP 
url prefix = /neighbor

SX-create_neighbor: POST, "/register"
    -needs the following input:
    {
    "name": "foo",
    "email": "foo@foo.foo",
    "phone": "1234567890",
    "zipcode": "12345"
    "username": "foofoo",
    "password": "foofoo"
    }

SX-login: POST, "neighbor/login"
    -requires the following payload:
    {
    "email": "foo@foo.foo",
    "password": "foofoo"
    }
SX-make_admin: PUT, "neighbor/admin/<neighbor_id>"
    -requires the following payload:
    {
    "admin": "1"
    }
SX-remove_admin: DELETE, "neighbor/admin/<neighbor_id>"
SX-get_neighbor_by_id: GET, "neighbor/get/id/<neighbor_id>"
SX-get_neighbor_by_username: GET, "neighbor/get/username/<username>"
SX-get_neighbor_by_email: GET, "neighbor/get/email/<email>"
SX-get_neighbor_by_zipcode: GET, "neighbor/get/zipcode/<zipcode>"
SX-update_neighbor: PUT, "neighbor/update/<neighbor_id>"
    -requires the following payload:
    {
    "first_name": "foo",
    "last_name": "foofoo",
    "email": "foo2@foo.foo",
    "phone": "1234567890",
    "zipcode": "12345"
    "username": "foofoo2",
    "password": "foofoo2",
    "admin": "False"
    }
SX-delete_neighbor: DELETE, "neighbor/delete/<neighbor_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FeedbackBP- 
url prefix = /feedback

SX-create_feedback: POST, "feedback/add"
    -requires the following payload:
    {
        "reviewed_neighbor_id": "<id_number>",
        "task_id": "<id_num>"
        "rating": "<rating_num>"
        "reviewer_id": "<reviewer_id_num>",
        "comment": "<string>"
    }
SX-get_feedback_by_id: GET, "feedback/get/<feedback_id>"
SX-get_feedback_by_task_id: GET, "feedback/get/task/<task_id>"
SX-get_feedback_by_neighbor_task_id: GET, "feedback/get/task_neighbor/<task_neighbor_id>"
SX-get_feedback_by_client_neighbor_id: GET, "feedback/get/client_neighbor/<client_neighbor_id>"
SX-update_task_neighbor_feedback_rating: PUT, "feedback/update/task_neighbor/<task_neighbor_id>"
SX-delete_feedback: DELETE, "feedback/delete/<feedback_id>"
SX-get_all_feedback: get, "feedback/get"


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TaskBP- url prefix = /task
SX-create_task: POST, "task/create"
    -requires the following payload:
    {
        "task_neighbor_id": "<int>",
        "client_neighbor_id": "<int>",
        "description": "string describing task",
        "skill_id": <int>,
        "task_paid": "<bool>",
        "traded_task": "<bool>"
    }
SX-get_all_tasks: GET, "task/get"
SX-get_task_by_id: GET, "task/get/<task_id>"
SX-get_task_by_task_neighbor_id: GET, "task/get/task_neighbor/<task_neighbor_id>"
SX-get_task_by_client_neighbor_id: GET, "task/get/client_neighbor/<client_neighbor_id>"
SX-update_task: PUT, "task/update/<task_id>" #updates task status
    -requires the following payload:
    {
        "client_neighbor_id": <int>,
        "task_neighbor_id": <int>,
        "description": "Cybersecurity stuff",
        "skill_id": <int>,
        "task_paid": "<bool>",
        "traded_task": "<bool>",
        "status": "in_progress, open, completed" 
}
SX-delete_task: DELETE, "task/delete/<task_id>/"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SkillBP
url prefix = /skill

SX-create_skill: POST, "/skill/create"
    -requires the following payload:
    {
        "name": "skill_name",
        "category": "skill_category",
        "experience": "beginner/intermediate/expert",
        "description": "skill_description"
    }
SX-get_all_skills: GET, "/skill/get"
SX-get_skill_by_id: GET, "/get/skill/<skill_id>"
SX-get_skill_by_name: GET, "/get/name/<name>"
SX-update_skill: PUT, "/skill/update/<skill_id>"
    -requires the following payload:
    {
        "name": "skill_name",
        "category": "skill_category",
        "experience": "beginner/intermediate/expert",
        "description": "skill_description"
    }
SX-delete_skill: DELETE, "/skill/delete/<skill_id>"

SX-get_neighbors_by_skill: GET, "/skill/get/<skill_id>/neighbors"
SX-add_skill_to_neighbor: POST, "skill/add/<skill_id>/neighbors/<neighbor_id>"
SX-remove_skill_from_neighbor: DELETE, "skill/remove/<skill_id>/neighbors/<neighbor_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PostBP
url prefix = /post

SX-create_post: POST, "post/add"
    requires the following payload:
    {
        "title": "post_title",
        "content": "post_content"
    }
SX-get_all_posts: GET, "post/get"
SX-get_post_by_id: GET, "post/get/<post_id>"
SX-get_posts_by_neighbor_id: GET, "post/get/neighbor/<neighbor_id>"
SX-update_post: PUT, "post/update/<post_id>"
SX-delete_post: DELETE, "post/delete/<post_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CommentBP
url prefix = /comment

SX-add_comment: POST, "comment/add"
    -requires the following payload:
    {
        "post_id": <post_id_num>,
        "content": "whatever you wanna comment here"
    }
SX-get_all_comments: GET, "comment/get"
SX-get_comment_by_id: GET, "comment/get/<comment_id>"
SX-get_comments_by_post_id: GET, "comment/get/post/<post_id>"
SX-get_comments_by_neighbor_id: GET, "comment/get/neighbor/<neighbor_id>"
SX-update_comment: PUT, "comment/update/<comment_id>"
    -requires the following payload:
    {
        "post_id": <post_id>,
        "content": "updated content"
    }
X-delete_comment: DELETE, "comment/delete/<comment_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

shareBP
-url prefix = /share

SX-add_share: POST, "share/add"
    -requires the following payload:
    {
        "post_id": <post_id>,
        "content": "post content"
    }
SX-get_share_by_id: GET, "share/get/<share_id>"
SX-update_share: PUT, "share/update/<share_id>"
SX-remove_share: DELETE, "share/remove/<share_id>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
likeBP 
-URL prefix = /like

SX-add_like: POST, "like/add"
SX-remove_like: DELETE, "like/delete/<like_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dislikeBP
-URL prefix = /dislike

SX-add_dislike: POST, "dislike/add"
SX-remove_dislike: DELETE, "dislike/remove/<dislike_id>