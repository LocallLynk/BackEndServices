LocalLynk Routes

This is to allow us to check off routes as we test them, so we know what works and what doesn't at a glance!

-mark working routes with an upper-case 'X' in front of the dash

NeighborBP 
url prefix = /neighbor

X-create_neighbor: POST, "/register"
    -needs the following input:
    {
    "name": "foo",
    "email": "foo@foo.foo",
    "phone": "1234567890",
    "zipcode": "12345"
    "username": "foofoo",
    "password": "foofoo"
    }

X-login: POST, "neighbor/login"
    -requires the following payload:
    {
    "email": "foo@foo.foo",
    "password": "foofoo"
    }
X-make_admin: PUT, "neighbor/admin/<neighbor_id>"
    -requires the following payload:
    {
    "admin": "1"
    }
X-remove_admin: DELETE, "neighbor/admin/<neighbor_id>"
X-get_neighbor_by_id: GET, "/<neighbor_id>"
X-get_neighbor_by_username: GET, "/username/<username>"
X-get_neighbor_by_email: GET, "email/<email>"
X-get_neighbor_by_zipcode: GET, "/zipcode/<zipcode>"
X-update_neighbor: PUT, "/<neighbor_id>"
    -requires the following payload:
    {
    "name": "foo2",
    "email": "foo2@foo.foo",
    "phone": "1234567890",
    "zipcode": "12345"
    "username": "foofoo2",
    "password": "foofoo2"
    }
X-delete_neighbor: DELETE, "/<neighbor_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FeedbackBP- 
url prefix = /feedback

X-create_feedback: POST, "feedback/add"
    -requires the following payload:
    {
        "reviewed_neighbor_id": "<id_number>",
        "task_id": "<id_num>"
        "rating": "<rating_num>"
        "reviewer_id": "<reviewer_id_num>",
        "comment": "<string>"
    }
X-get_feedback_by_id: GET, "feedback/get/<feedback_id>"
X-get_feedback_by_task_id: GET, "feedback/get/task/<task_id>"
X-get_feedback_by_neighbor_task_id: GET, "feedback/get/task_neighbor/<task_neighbor_id>"
X-get_feedback_by_client_neighbor_id: GET, "feedback/get/client_neighbor/<client_neighbor_id>"
X-update_task_neighbor_feedback_rating: PUT, "feedback/update/task_neighbor/<task_neighbor_id>"
X-delete_feedback: DELETE, "feedback/delete/<feedback_id>"
X-get_all_feedback: get, "feedback/get"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SkillBP
url prefix = /skill
X-create_skill: POST, "/"
    -requires the following payload:
    {
        "name": "skill name",
        "category": "skill category",
        "experience": "beginner, intermediate, etc",
        "description": "skill description"
    }
X-get_all_skills: GET, "/"
X-get_skill_by_id: GET, "/<skill_id>"
X-get_skill_by_name: GET, "/name/<name>"
X-update_skill: PUT, "/<skill_id>"
    -requires the following payload:
    {
        "name": "skill name",
        "category": "skill category",
        "experience": "beginner, intermediate, etc",
        "description": "skill description"
    }
X-delete_skill: DELETE, "/<skill_id>
X-get_neighbors_by_skill: GET, "skill/get/<skill_id>/neighbors"
X-remove_skill_by_neighbor: DELETE, "skill/remove/<skill_id>/neighbors/<neighbor_id>"
X-add_skill_to_neighbors: POST, "skill/add/<skill_id>/neighbors/<neighbor_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TaskBP- url prefix = /task
X-create_task: POST, "task/create"
    -requires the following payload:
    {
        "task_neighbor_id": "<int>",
        "client_neighbor_id": "<int>",
        "description": "string describing task",
        "skill_id": <int>,
        "task_paid": "<bool>",
        "traded_task": "<bool>"
    }
X-get_all_tasks: GET, "task/get"
X-get_task_by_id: GET, "task/get/<task_id>"
X-get_task_by_task_neighbor_id: GET, "task/get/task_neighbor/<task_neighbor_id>"
X-get_task_by_client_neighbor_id: GET, "task/get/client_neighbor/<client_neighbor_id>"
X-update_task: PUT, "task/update/<task_id>" #updates task status
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
X-delete_task: DELETE, "task/delete/<task_id>/"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SkillBP
url prefix = /skill

X-create_skill: POST, "/skill/create"
    -requires the following payload:
    {
        "name": "skill_name",
        "category": "skill_category",
        "experience": "beginner/intermediate/expert",
        "description": "skill_description"
    }
X-get_all_skills: GET, "/skill/get"
X-get_skill_by_id: GET, "/get/skill/<skill_id>"
X-get_skill_by_name: GET, "/get/name/<name>"
X-update_skill: PUT, "/skill/update/<skill_id>"
    -requires the following payload:
    {
        "name": "skill_name",
        "category": "skill_category",
        "experience": "beginner/intermediate/expert",
        "description": "skill_description"
    }
X-delete_skill: DELETE, "/skill/delete/<skill_id>"

X-get_neighbors_by_skill: GET, "/skill/get/<skill_id>/neighbors"
X-add_skill_to_neighbor: POST, "skill/add/<skill_id>/neighbors/<neighbor_id>"
X-remove_skill_from_neighbor: DELETE, "skill/remove/<skill_id>/neighbors/<neighbor_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FeedbackBP
url prefix = /feedback

X-create_feedback: POST, "feedback/add"
    -requires the following payload:
    {
        "reviewed_neighbor_id": <reviewed_neighbor_id>,
        "task_id": <task_id>,
        "rating": <rating_int>,
        "reviewer_id": <reviewer_id>,
        "comment": "whatever feedback you want to leave goes here"
    }
X-get_feedback_by_id: GET, "feedback/get/<feedback_id>"
X-get_feedback_by_task_id: GET, "feedback/get/task/<task_id>"
X-get_feedback_by_task_neighbor_id: GET, "feedback/get/task_neighbor/<task_neighbor_id>"
X-get_feedback_by_client_neighbor_id: GET, "feedback/get/client_neighbor/<client_neighbor_id>"
X-delete_feedback: DELETE, "feedback/delete/<feedback_id>"
X-get_all_feedback: GET, "feedback/get"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PostBP
url prefix = /post

X-create_post: POST, "post/add"
    requires the following payload:
    {
        "title": "post_title",
        "content": "post_content"
    }
X-get_all_posts: GET, "post/get"
X-get_post_by_id: GET, "post/get/<post_id>"
X-get_posts_by_neighbor_id: GET, "post/get/neighbor/<neighbor_id>"
X-update_post: PUT, "post/update/<post_id>"
X-delete_post: DELETE, "post/delete/<post_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CommentBP
url prefix = /comment

X-add_comment: POST, "comment/add"
    -requires the following payload:
    {
        "post_id": <post_id_num>,
        "content": "whatever you wanna comment here"
    }
X-get_all_comments: GET, "comment/get"
X-get_comment_by_id: GET, "comment/get/<comment_id>"
X-get_comments_by_post_id: GET, "comment/get/post/<post_id>"
X-get_comments_by_neighbor_id: GET, "comment/get/neighbor/<neighbor_id>"
X-update_comment: PUT, "comment/update/<comment_id>"
    -requires the following payload:
    {
        "post_id": <post_id>,
        "content": "updated content"
    }
X-delete_comment: DELETE, "comment/delete/<comment_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

shareBP
-url prefix = /share

X-add_share: POST, "share/add"
    -requires the following payload:
    {
        "post_id": <post_id>,
        "content": "post content"
    }
X-get_share_by_id: GET, "share/get/<share_id>"
X-update_share: PUT, "share/update/<share_id>"
X-remove_share: DELETE, "share/remove/<share_id>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
likeBP 
-URL prefix = /like

X-add_like: POST, "like/add"
X-remove_like: DELETE, "like/delete/<like_id>"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dislikeBP
-URL prefix = /dislike

X-add_dislike: POST, "dislike/add"
X-remove_dislike: DELETE, "dislike/remove/<dislike_id>