from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://app:testing@localhost:5432/library_api"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db  