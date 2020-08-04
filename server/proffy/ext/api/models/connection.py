from proffy.ext.db import db

class ConnectionModel(db.Model):
    __tablename__ = "connections"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)