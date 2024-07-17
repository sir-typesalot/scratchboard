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
    board_model = BoardModel().get({'hash' : hash})
    variables['hash'] = board_model.hash
    variables['name'] = board_model.name
    variables['create_datatime'] = board_model.create_datetime
    variables['is_active'] = board_model.is_active 
    return render_template('board.html', data=variables)

@board.route('/board/<string:hash>/modify', methods=['POST'])
def modify_board(hash):
    # TODO: Modify the baord and return the data to be rendered into the page
    return render_template('board.html', data=variables)

@board.route('/board/<string:hash>/delete', methods=['DELETE'])
def delete_board(hash):
    # TODO: delete board and return status, then route to home page
    redirect(url_for('public.home'))
