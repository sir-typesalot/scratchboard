from flask import redirect, request, Blueprint, render_template, url_for

external = Blueprint('public', __name__)

variables = {
    'title': 'Home',
    'footer_text': 'Gym-Journal',
    'cache': 1
}

@external.route('/', methods=['GET'])
def public():
    return render_template('home.html', data=variables)

@external.route('/login', methods=['GET', 'POST'])
def login():
    variables['title'] = "Login"
    return render_template('login.html', data=variables)

@external.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        variables['title'] = "Sign Up"
        return render_template('signup.html', data=variables)
    else:
        # Create account
        return redirect(url_for('login'))
