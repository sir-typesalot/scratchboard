"""
    Import the app object from routes and make accessible to higher levels.
"""
from flask import Flask
from .routes import tags, board, endpoints

webapp = Flask(
    __name__,
    template_folder='frontend/templates',
    static_folder='frontend/static'
)
webapp.secret_key = '93843hserj39sfsw3'
webapp.register_blueprint(endpoints)
webapp.register_blueprint(board)
webapp.register_blueprint(tags)
