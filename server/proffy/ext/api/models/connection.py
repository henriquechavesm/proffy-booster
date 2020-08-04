from proffy.ext.db import db

class ConnectionModel(db.Model):
    __tablename__ = "connections"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, created_at, user_id):
        self.created_at = created_at
        self.user_id = user_id
    
    @classmethod
    def count_connections(cls):
        return cls.query.count()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()