from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

db = SQLAlchemy()


class Login(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class User(db.Model):

    __tablename__ = "Iris"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SepalLengthCm = db.Column(db.Integer, nullable=False)
    SepalWidthCm = db.Column(db.Integer, nullable=False)
    PetalLengthCm = db.Column(db.Integer, nullable=False)
    PetalWidthCm = db.Column(db.Integer, nullable=False)                     
    Species = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User Id={self.Id} SepalLengthCm={self.SepalLengthCm} SepalWidthCm={self.SepalWidthCm} PetalLengthCm={self.PetalLengthCm} PetalWidthCm={self.PetalWidthCm} Species={self.Species}'


def connect_to_db(flask_app, db_uri='sqlite:///database_iris.db', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)
    db.create_all(app=flask_app)
    print('Connected to the db!')





if __name__ == "__main__":
    from server import app
