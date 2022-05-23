from model import db, User


def create_user(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species):

    user = User(SepalLengthCm=SepalLengthCm, SepalWidthCm=SepalWidthCm, PetalLengthCm=PetalLengthCm, PetalWidthCm=PetalWidthCm, Species=Species)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Returns all users in database"""
    
    return User.query.all()


def get_user_by_id(Id):
    """Returns a user by id"""

    return User.query.filter(User.Id == Id).first()


def update_user(Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species):
    """Updates a user by id"""

    user = get_user_by_id(Id)
    user.SepalLengthCm = SepalLengthCm
    user.SepalWidthCm = SepalWidthCm
    user.PetalLengthCm = PetalLengthCm
    user.PetalWidthCm = PetalWidthCm
    user.Species = Species

    db.session.add(user)
    db.session.commit()

    return user


def delete_user(Id):
    """Deletes a user by id"""

    User.query.filter(User.Id == Id).delete()

    return db.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
