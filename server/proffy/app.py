from flask import Flask

from proffy.ext import config
from proffy.ext import db
from proffy.ext import api
from proffy.ext import hooks


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    api.init_app(app)
    hooks.init_app(app)

    return app