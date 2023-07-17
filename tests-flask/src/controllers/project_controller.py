from flask import Blueprint, render_template, request, redirect
from models.projectModel import ProjectModel
from models.querys import _project_id, _task_id

project_controller = Blueprint('project', __name__)


def _get_project_or_task(id):
    project = ProjectModel.find(id)
    return [task.to_dict() for task in project]


def _format_date(date):
    splited = date.split('-')
    splited.reverse()
    return '/'.join(splited)


def _save_task(req, id_project, name_project):
    deadline = {
        'idProject': int(id_project),
        'name': name_project,
        'task': req.get('name'),
        'status': req.get('status'),
        'completionPercentage': req.get('percentage'),
        'descriptionTask': req.get('description'),
        'deadline': _format_date(req.get('deadline')),
        'responsible': req.get('responsible')
    }
    task = ProjectModel(deadline)
    task.save()


@project_controller.route("/")
@project_controller.route("/projects")
def home():
    projects = ProjectModel.separate_projects()
    return render_template("home.html", projects=projects)


@project_controller.route("/projects/<id>")
def project(id):
    if id.isnumeric():
        project = _get_project_or_task(_project_id(id))
        return render_template("project.html", project=project)
    return render_template('notFound.html'), 404


@project_controller.route("/task/<id>")
def task(id):
    if id.isalnum():
        task = _get_project_or_task(_task_id(id))
        return render_template("task.html", task=task[0])
    return render_template('notFound.html'), 404


@project_controller.route(
    "/task/<id_project>/form",
    methods=['GET', 'POST']
)
def new_task(id_project):
    if request.method == 'POST':
        project = _get_project_or_task(_project_id(id_project))
        _save_task(request.form, id_project, project[0]['name'])
        return redirect("http://127.0.0.1:8000/", code=302)
    if id_project.isnumeric():
        return render_template('taskForm.html')
    return render_template('notFound.html'), 404


# @project_controller.route(
#     "/task/<id>/delete",
#     methods=['POST']
# )
# def task_delete(id):
#     task = ProjectModel.find(_task_id(id))
#     print(task)
#     if task[0] is None:
#         return render_template('notFound.html'), 404
#     else:
#         ProjectModel.delete(_id=task[0]['_id'])
#         return redirect("http://127.0.0.1:8000/", code=302)
