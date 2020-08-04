from flask import Blueprint
from flask_restful import Api

from proffy.ext.api.resources.classes import Classes
from proffy.ext.api.resources.connections import Connections

bp = Blueprint("api", __name__)
api = Api(bp)


api.add_resource(Classes, "/classes")
api.add_resource(Connections, "/connections")