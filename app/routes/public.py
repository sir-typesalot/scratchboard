from flask import redirect, request, Blueprint, render_template, url_for
from lib.models import BoardModel

endpoints = Blueprint('app', __name__)

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
    id = bm.create_new(seed, name)
    if id:
        board = bm.get({'id': id})
        return redirect(url_for('app.board', hash=board.hash))
    else:
        return render_template('error.html', data=variables)

@endpoints.route('/board/<string:hash>', methods=['GET'])
def board(hash):
    variables['title'] = "Create A Board"
    return render_template('board.html', data=variables)
