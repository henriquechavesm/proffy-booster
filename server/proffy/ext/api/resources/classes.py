from flask_restful import Resource, reqparse

from proffy.ext.api.models.user import UserModel
from proffy.ext.api.models.classes import ClassModel, ClassScheduleModel

from proffy.utils import convert_to_minutes


BLANK_ERROR = "This field cannot be left blank!"
INTERNAL_ERROR = "An internal error ocurred. Try again."

class Classes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help=BLANK_ERROR)
    parser.add_argument("avatar", type=str, required=True, help=BLANK_ERROR)
    parser.add_argument("whatsapp", type=str, required=True, help=BLANK_ERROR)
    parser.add_argument("bio", type=str, required=True, help=BLANK_ERROR)
    parser.add_argument("subject", type=str, required=True, help=BLANK_ERROR)
    parser.add_argument("cost", type=float, required=True, help=BLANK_ERROR)
    parser.add_argument("schedule", type=dict, action="append", required=False, help=BLANK_ERROR)


    def get(self):
        return {"message": "Hello World CLASSES"}
    
    def post(self):
        data = Classes.parser.parse_args()

        user = UserModel.find_user_by_whatsapp(data["whatsapp"])
        if not user:
            try:
                user = UserModel(data["name"], data["avatar"], data["whatsapp"], data["bio"])
                user.save_to_db()
            except:
                return {"message": INTERNAL_ERROR}, 500

        try:
            class_general = ClassModel(data["subject"], data["cost"], user.id)
            class_general.save_to_db()
        except:
            return {"message": INTERNAL_ERROR}, 500

        try:
            for schedule in data["schedule"]:
                schedule["from_hour"] = convert_to_minutes(schedule["from_hour"])
                schedule["to_hour"] = convert_to_minutes(schedule["to_hour"])
                class_schedule = ClassScheduleModel(**schedule, class_id=class_general.id)
                class_schedule.save_to_db()
        except:
            class_general.delete_from_db()
            return {"message": INTERNAL_ERROR}, 500

        return data, 201