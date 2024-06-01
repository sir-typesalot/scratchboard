from flask import redirect, request, Blueprint, render_template, url_for

external = Blueprint('public', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@external.route('/', methods=['GET'])
def public():
    return render_template('home.html', data=variables)

@external.route('/create-board', methods=['GET', 'POST'])
def login():
    variables['title'] = "Create A Board"
    return render_template('login.html', data=variables)
