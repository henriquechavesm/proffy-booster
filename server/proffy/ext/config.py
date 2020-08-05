def init_app(app):
    app.config["SECRET_KEY"] = "proffy"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///proffy.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False