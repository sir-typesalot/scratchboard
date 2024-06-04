from flask import redirect, Blueprint, render_template, url_for
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

@board.route('/board/<string:hash>/modify', methods=['POST'])
def modify_board(hash):
    variables['title'] = "Project Board"
    return render_template('board.html', data=variables)

@board.route('/board/<string:hash>/delete', methods=['DELETE'])
def delete_board(hash):
    variables['title'] = "Project Board"
    redirect(url_for('public.home'))
