from proffy.ext.db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    avatar = db.Column(db.String(200), nullable=False)
    whatsapp = db.Column(db.String(80), nullable=False, unique=True)
    bio = db.Column(db.String(500), nullable=False)
    classes = db.relationship("ClassModel", lazy="dynamic", cascade="all, delete-orphan")
    # connections = db.relationship("ConnectionModel", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, name, avatar, whatsapp, bio):
        self.name = name
        self.avatar = avatar
        self.whatsapp = whatsapp
        self.bio = bio

    def json(self):
        {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar,
            "whatsapp": self.whatsapp,
            "bio": self.bio,
            # "classes": [class.json() for class in self.classes]
        }

    @classmethod
    def find_all_users(cls):
        return cls.query.all()

    @classmethod
    def find_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_user_by_whatsapp(cls, whatsapp):
        return cls.query.filter_by(whatsapp=whatsapp).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()