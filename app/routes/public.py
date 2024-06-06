from flask import redirect, request, Blueprint, render_template, url_for
from lib.models import BoardModel

endpoints = Blueprint('public', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@endpoints.route('/', methods=['GET'])
def home():
    return render_template('home.html', data=variables)

@endpoints.route('/create-board', methods=['POST'])
def create_board():
    bm = BoardModel()
    seed = request.json.get('seed')
    name = request.json.get('name')
    # TODO: Need to add checks for seed and name on JS side
    try:
        id = bm.create_new(seed, name)
    except:
        # TODO: need to figured out how to handle the errors
        pass

    if not id:
        return render_template('error.html', data=variables)

    board = bm.get({'id': id})
    return redirect(url_for('board.get_board', hash=board.hash))
