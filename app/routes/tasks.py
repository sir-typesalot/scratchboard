from flask import request, Blueprint, render_template
from lib.models.TaskModel import TaskModel

tasks = Blueprint('task', __name__, url_prefix='/board')

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@tasks.route('/<string:hash>/tasks', methods=['GET'])
def get_tasks(hash):
    task_model = TaskModel(hash)
    tasks = task_model.get()
    return tasks

@tasks.route('/<string:hash>/task/<int:task_id>', methods=['GET'])
def get_task(hash, task_id):
    task_model = TaskModel(hash)
    task = task_model.get({'task_id': task_id})
    return task[0] if task else []

@tasks.route('/<string:hash>/task/new', methods=['POST'])
def create_task(hash):
    task_model = TaskModel(hash)
    # Get params
    title = request.json.get('title')
    description = request.json.get('description')
    tag_id = request.json.get('tag_id')

    tags = task_model.create(title, description, tag_id)
    return tags

@tasks.route('/<string:hash>/task/<int:task_id>/modify', methods=['PUT'])
def modify_task(hash, task_id):
    return {}

@tasks.route('/<string:hash>/task/<int:task_id>/delete', methods=['DELETE'])
def delete_task(hash, task_id):
    return render_template('error.html', data=variables)
