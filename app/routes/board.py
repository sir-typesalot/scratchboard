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
    # TODO: get board from hash, use board.id to get the tasks and tags for board
    # No need to get comments, we won't see that here
    return render_template('board.html', data=variables)

@board.route('/board/<string:hash>/modify', methods=['POST'])
def modify_board(hash):
    # TODO: Modify the baord and return the data to be rendered into the page
    return render_template('board.html', data=variables)

@board.route('/board/<string:hash>/delete', methods=['DELETE'])
def delete_board(hash):
    # TODO: delete board and return status, then route to home page
    redirect(url_for('public.home'))
