from models.user import User
from db import db

def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user