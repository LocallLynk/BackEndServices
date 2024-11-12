LocalLynk Routes

This is to allow us to check off routes as we test them, so we know what works and what doesn't at a glance!

-mark working routes with an upper-case 'X' in front of the dash

NeighborBP- url prefix /neighbor

X-create_neighbor: POST, "/"
X-get_all_neighbors: GET. "/"
X-login: POST, "neighbor/login"
X-make_admin: PUT, "neighbor/admin/<neighbor_id>"
X-remove_admin: DELETE, "neighbor/admin/<neighbor_id>"
X-get_neighbor_by_id: GET, "/<neighbor_id>"
X-get_neighbor_by_username: GET, "/username/<username>"
X-get_neighbor_by_email: GET, "email/<email>"
X-get_neighbor_by_zipcode: GET, "/zipcode/<zipcode>"
X-update_neighbor: PUT, "/<neighbor_id>"
X-delete_neighbor: DELETE, "/<neighbor_id>"

FeedbackBP- url prefix /feedback

-create_feedback: POST, "/"
-get_feedback_by_id: GET, "/<feedback_id>"
-get_feedback_by_task_id: GET, "/task/<task_id>"
-get_feedback_by_neighbor_task_id: GET, "/task_neighbor/<task_neighbor_id>"
-get_feedback_by_client_neighbor_id: GET, "/client_neighbor/<client_neighbor_id>"
-update_task_neighbor_feedback_rating: PUT, "/task_neighbor/<task_neighbor_id>"
-update_client_neighbor_feedback_rating: PUT, "/client_neighbor/<client_neighbor_id>"
-delete_feedback: DELETE, "/<feedback_id>"
-get_all_feedback: get, "/"

SkillBP- url prefix /skill

X-create_skill: POST, "/"
X-get_all_skills: GET, "/"
X-get_skill_by_id: GET, "/<skill_id>"
X-get_skill_by_name: GET, "/name/<name>"
X-update_skill: PUT, "/<skill_id>"
X-delete_skill: DELETE, "/<skill_id>
X-get_neighbors_by_skill: GET, "/<skill_id>/neighbors"
X-remove_skill_by_neighbor: DELETE, "/<skill_id>/neighbors/<neighbor_id>"
X-_add_skill_to_neighbors: POST, "/<skill_id>/neighbors/     <neighbor_id>"

TaskBP- url prefix /task
-create_task: POST, "/"
-get_all_tasks: GET, "/"
-get_task_by_id: GET, "/<task_id>"
-get_task_by_task_neighbor_id: GET, "/task_neighbor/<task_neighbor_id>"
-get_task_by_client_neighbor_id: GET, "/client_neighbor/<client_neighbor_id>"
-update_task: PUT, "/<task_id>"
-delete_task: DELETE, "/<task_id>/"