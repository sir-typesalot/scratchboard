from flask import jsonify, request, Blueprint, render_template
from lib.models.TaskModel import TaskModel
from lib.models.TagModel import TagModel
from app.decorators import make_response

tasks = Blueprint('task', __name__, url_prefix='/board')

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@tasks.route('/<string:hash>/tasks', methods=['GET'])
@make_response
def get_tasks(hash):
    task_model = TaskModel(hash)
    tasks = task_model.get()
    return tasks

@tasks.route('/<string:hash>/tasks/<int:task_id>', methods=['GET'])
def get_task(hash, task_id):
    task_model = TaskModel(hash)
    task = task_model.get({'task_id': task_id})
    task = task[0] if task else []
    return jsonify(task)

@tasks.route('/<string:hash>/tasks/new', methods=['POST'])
def create_task(hash):
    task_model = TaskModel(hash)
    response = {}
    # Get params
    title = request.json.get('title')
    description = request.json.get('description')
    tag_name = request.json.get('tag')
    status = request.json.get('status')
    due_date = request.json.get('dueDate')

    # TODO: We need to handle when a tag doesn't exist, ie. create it
    # Then pass the id down to create task
    tag = TagModel(hash).get({'tag_name': tag_name}, fetchone=True)

    try:
        response['task_id'] = task_model.create(title, description, tag.tag_id)
        status = 200
    except NameError:
        response['task_id'] = None
        status = 302

    return jsonify(response), status

@tasks.route('/<string:hash>/tasks/<int:task_id>/modify', methods=['PUT'])
def modify_task(hash, task_id):
    return {}

@tasks.route('/<string:hash>/tasks/<int:task_id>/delete', methods=['DELETE'])
def delete_task(hash, task_id):
    return render_template('error.html', data=variables)
