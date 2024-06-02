from flask import redirect, request, Blueprint, render_template, url_for

endpoints = Blueprint('app', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@endpoints.route('/', methods=['GET'])
def public():
    return render_template('home.html', data=variables)

@endpoints.route('/create-board', methods=['POST'])
def login():
    return redirect(url_for('app.board', hash='e'))

@endpoints.route('/board/<string:hash>', methods=['GET'])
def board(hash):
    variables['title'] = "Create A Board"
    return render_template('board.html', data=variables)
