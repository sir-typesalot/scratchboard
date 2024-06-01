from flask import render_template, Blueprint

internal = Blueprint('private', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@internal.route('/private')
def private():
    return "helllo"

# TODO: Need to specify the type/format of the hash
@internal.route('/board/<hash>', methods=['GET'])
def create_routine():
    return render_template('new_routine.html', data=variables)
