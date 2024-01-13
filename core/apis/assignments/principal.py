from flask import Blueprint,jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.teachers import Teacher

from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignment_resources = Blueprint('principal_assignment_resources',__name__)

@principal_assignment_resources.route("/assignments",methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    students_assignments = Assignment.get_assignments_by_principal(p.principal_id)
    students_assignments_dump = AssignmentSchema().dump(students_assignments,many=True)
    # assignments_json = [assignment.__dict__ for assignment in students_assignments]

    # for assignment_dict in assignments_json:
    #     assignment_dict.pop('_sa_instance_state', None)
    
    return APIResponse.respond(data=students_assignments_dump)

@principal_assignment_resources.route("/teachers",methods=['GET'],strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    teachers = Teacher.all_teachers(p.principal_id)

    teachers_json = [teacher.__dict__ for teacher in teachers]

    for teacher_dict in teachers_json:
        teacher_dict.pop('_sa_instance_state', None)
    return APIResponse.respond(data=teachers_json)

@principal_assignment_resources.route("/assignments/grade",methods=['POST'],strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p,incoming_payload):
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id = grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
