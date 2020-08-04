from flask_restful import Resource, reqparse

from proffy.ext.api.models.user import UserModel
from proffy.ext.api.models.classes import ClassModel, ClassScheduleModel

from proffy.utils import convert_to_minutes


BLANK_ERROR = "This field cannot be left blank!"
INTERNAL_ERROR = "An internal error ocurred. Try again."

class Classes(Resource):
    body_parser = reqparse.RequestParser()
    body_parser.add_argument("name", type=str, required=True, help=BLANK_ERROR)
    body_parser.add_argument("avatar", type=str, required=True, help=BLANK_ERROR)
    body_parser.add_argument("whatsapp", type=str, required=True, help=BLANK_ERROR)
    body_parser.add_argument("bio", type=str, required=True, help=BLANK_ERROR)
    body_parser.add_argument("subject", type=str, required=True, help=BLANK_ERROR)
    body_parser.add_argument("cost", type=float, required=True, help=BLANK_ERROR)
    body_parser.add_argument("schedule", type=dict, action="append", required=False, help=BLANK_ERROR)

    query_parser = reqparse.RequestParser()
    query_parser.add_argument("week_day", type=int)
    query_parser.add_argument("subject", type=str)
    query_parser.add_argument("time", type=str)


    def get(self):
        query_data = Classes.query_parser.parse_args()
        
        if not query_data["week_day"] or not query_data["subject"] or not query_data["time"]:
            return {"message": "Missing filters to search classes."}, 400
    
        class_time = convert_to_minutes(query_data["time"])

        classes_filtered = ClassModel.query.filter_by(subject=query_data["subject"]).filter(ClassScheduleModel.from_hour <= class_time).filter(ClassScheduleModel.to_hour > class_time).filter(ClassScheduleModel.week_day==query_data["week_day"]).all()

        classes_with_teachers = [{**class_filtered.json(), **class_filtered.user.json()} for class_filtered in classes_filtered]

        return classes_with_teachers, 200
    
    def post(self):
        body_data = Classes.body_parser.parse_args()

        user = UserModel.find_user_by_whatsapp(body_data["whatsapp"])
        if not user:
            try:
                user = UserModel(body_data["name"], body_data["avatar"], body_data["whatsapp"], body_data["bio"])
                user.save_to_db()
            except:
                return {"message": INTERNAL_ERROR}, 500

        try:
            class_general = ClassModel(body_data["subject"], body_data["cost"], user.id)
            class_general.save_to_db()
        except:
            return {"message": INTERNAL_ERROR}, 500

        try:
            for schedule in body_data["schedule"]:
                schedule["from_hour"] = convert_to_minutes(schedule["from_hour"])
                schedule["to_hour"] = convert_to_minutes(schedule["to_hour"])
                class_schedule = ClassScheduleModel(**schedule, class_id=class_general.id)
                class_schedule.save_to_db()
        except:
            class_general.delete_from_db()
            return {"message": INTERNAL_ERROR}, 500

        return body_data, 201