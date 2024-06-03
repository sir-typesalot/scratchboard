from flask import redirect, request, Blueprint, render_template, url_for
from lib.models import BoardModel

board = Blueprint('board', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@board.route('/board/<string:hash>', methods=['GET'])
def get_board(hash):
    variables['title'] = "Project Board"
    return render_template('board.html', data=variables)
