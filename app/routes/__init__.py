from flask import Flask

from .public import app

webapp = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)
webapp.secret_key = '93843hserj39sfsw3'
webapp.register_blueprint(app)
