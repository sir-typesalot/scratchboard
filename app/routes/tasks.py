from flask import redirect, request, Blueprint, render_template, url_for

tasks = Blueprint('task', __name__, url_prefix='/board')

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@tasks.route('/<string:hash>/tasks', methods=['GET'])
def get_tasks(hash):
    return render_template('error.html', data=variables)

@tasks.route('/<string:hash>/task/<int:task_id>', methods=['GET'])
def get_task(hash, task_id):
    return render_template('error.html', data=variables)

@tasks.route('/<string:hash>/task/new', methods=['POST'])
def create_task(hash):
    return render_template('error.html', data=variables)

@tasks.route('/<string:hash>/task/<int:task_id>/modify', methods=['PUT'])
def modify_task(hash, task_id):
    return render_template('error.html', data=variables)

@tasks.route('/<string:hash>/task/<int:task_id>/delete', methods=['DELETE'])
def delete_task(hash, task_id):
    return render_template('error.html', data=variables)
