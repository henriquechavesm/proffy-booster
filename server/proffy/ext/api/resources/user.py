from flask_restful import Resource
from proffy.ext.api.models.user import UserModel


class User(Resource):

    @classmethod
    def get(cls, whatsapp):
        return {"message":"GET Ok"}, 200
    
    @classmethod
    def post(cls, whatsapp):
        return {"message": "POST Ok"}, 200


class UserList(Resource):
    
    @classmethod
    def get(cls):
        users = UserModel.find_all_users()
        return {"users": [user.json() for user in users]}, 200