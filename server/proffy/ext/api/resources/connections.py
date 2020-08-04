from flask_restful import Resource, reqparse
from datetime import datetime
from proffy.ext.api.models.connection import ConnectionModel

BLANK_ERROR = "This field cannot be left blank!"
INTERNAL_ERROR = "An internal error ocurred. Try again."


class Connections(Resource):
    body_parser = reqparse.RequestParser()
    body_parser.add_argument("user_id", type=int, required=True, help=BLANK_ERROR)

    def get(self):
        n_connections = ConnectionModel.count_connections()
        return {"total": n_connections}, 200

    def post(self):
        body_data = Connections.body_parser.parse_args()
        time_now = int(datetime.now().strftime("%Y%m%d%H%M%S"))

        try:
            new_connection = ConnectionModel(time_now, body_data["user_id"])
            new_connection.save_to_db()
        except:
            return {"message: INTERNAL_ERROR"}, 500
        
        return {"message": "A new connection was created."}, 201