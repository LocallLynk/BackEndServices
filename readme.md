LocalLynk Routes

This is to allow us to check off routes as we test them, so we know what works and what doesn't at a glance!

-mark working routes with an upper-case 'X' in front of the dash

NeighborBP- url prefix /neighbor

-create_neighbor: POST, "/"
    -needs the following input:
    {
    "name": "foo",
    "email": "foo@foo.foo",
    "phone": "1234567890",
    "zipcode": "12345"
    "username": "foofoo",
    "password": "foofoo"
    }

-get_all_neighbors: GET. "/"
-login: POST, "neighbor/login"
    -needs the following input:
    {
    "email": "foo@foo.foo",
    "password": "foofoo"
    }
-make_admin: PUT, "neighbor/admin/<neighbor_id>"
    -needs the following input:
    {
    "admin": "1"
    }
-remove_admin: DELETE, "neighbor/admin/<neighbor_id>"
-get_neighbor_by_id: GET, "/<neighbor_id>"
-get_neighbor_by_username: GET, "/username/<username>"
-get_neighbor_by_email: GET, "email/<email>"
-get_neighbor_by_zipcode: GET, "/zipcode/<zipcode>"
-update_neighbor: PUT, "/<neighbor_id>"
    -needs the following input:
    {
    "name": "foo2",
    "email": "foo2@foo.foo",
    "phone": "1234567890",
    "zipcode": "12345"
    "username": "foofoo2",
    "password": "foofoo2"
    }
-delete_neighbor: DELETE, "/<neighbor_id>"

FeedbackBP- url prefix /feedback

-create_feedback: POST, "/"
    -needs the following input:
    {
        "reviewed_neighbor_id": "<id_number>",
        "task_id": "<id_num>"
        "rating": "<rating_num>"
        "reviewer_id": "<reviewer_id_num>",
        "comment": "<string>"
    }
-get_feedback_by_id: GET, "/<feedback_id>"
-get_feedback_by_task_id: GET, "/task/<task_id>"
-get_feedback_by_neighbor_task_id: GET, "/task_neighbor/<task_neighbor_id>"
-get_feedback_by_client_neighbor_id: GET, "/client_neighbor/<client_neighbor_id>"
-update_task_neighbor_feedback_rating: PUT, "/task_neighbor/<task_neighbor_id>"
-update_client_neighbor_feedback_rating: PUT, "/client_neighbor/<client_neighbor_id>"
-delete_feedback: DELETE, "/<feedback_id>"
-get_all_feedback: get, "/"

SkillBP- url prefix /skill

-create_skill: POST, "/"
    -requires the following input:
    {
        "name": "skill name",
        "category": "skill category",
        "experience": "beginner, intermediate, etc",
        "description": "skill description"
    }
-get_all_skills: GET, "/"
-get_skill_by_id: GET, "/<skill_id>"
-get_skill_by_name: GET, "/name/<name>"
-update_skill: PUT, "/<skill_id>"
    -requires the following input:
    {
        "name": "skill name",
        "category": "skill category",
        "experience": "beginner, intermediate, etc",
        "description": "skill description"
    }
-delete_skill: DELETE, "/<skill_id>
-get_neighbors_by_skill: GET, "/<skill_id>/neighbors"
-remove_skill_by_neighbor: DELETE, "/<skill_id>/neighbors/<neighbor_id>"
-_add_skill_to_neighbors: POST, "/<skill_id>/neighbors/     <neighbor_id>"

TaskBP- url prefix /task
-create_task: POST, "/"
    -requires the following input:
    {
        "task_neighbor_id": "<int>",
        "client_neighbor_id": "<int>",
        "description": "string describing task",
        "skill_id": <int>,
        "task_paid": "<bool>",
        "traded_task": "<bool>"
    }
-get_all_tasks: GET, "/"
-get_task_by_id: GET, "/<task_id>"
-get_task_by_task_neighbor_id: GET, "/task_neighbor/<task_neighbor_id>"
-get_task_by_client_neighbor_id: GET, "/client_neighbor/<client_neighbor_id>"
-update_task: PUT, "/<task_id>"
    -requires the following input:
    {
        "client_neighbor_id": <int>,
        "task_neighbor_id": <int>,
        "description": "Cybersecurity stuff",
        "skill_id": <int>,
        "task_paid": "<bool>",
        "traded_task": "<bool>",
        "status": "closed"
}
-delete_task: DELETE, "/<task_id>/"