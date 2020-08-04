from proffy.ext.db import db

class ClassModel(db.Model):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("UserModel")
    classes_schedule = db.relationship("ClassScheduleModel", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, subject, cost, user_id):
        self.subject = subject
        self.cost = cost
        self.user_id = user_id
    
    def json(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "cost": self.cost,
            "user_id": self.user_id
        }


class ClassScheduleModel(db.Model):
    __tablename__ = "classes_schedule"
    id = db.Column(db.Integer, primary_key=True)
    week_day = db.Column(db.Integer, nullable=False)
    from_hour = db.Column(db.Integer, nullable=False)
    to_hour = db.Column(db.Integer, nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("classes.id"), nullable=False)