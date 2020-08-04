from flask import Blueprint
from flask_restful import Api

from proffy.ext.api.resources.user import User, UserList
from proffy.ext.api.resources.classes import Classes

bp = Blueprint("api", __name__)
api = Api(bp)


api.add_resource(User, "/user/<string:whatsapp>")
api.add_resource(UserList, "/users")
api.add_resource(Classes, "/classes")