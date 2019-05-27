from app.models import db, User


def registrate_user(data):
    usr = User(**data)
    import ipdb; ipdb.set_trace()
    db.session.add(usr)
    db.session.commit()
