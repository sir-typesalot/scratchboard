from flask import jsonify
from functools import wraps

def make_response(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)
        return jsonify({
            'data': result
        })
    return decorated_function
