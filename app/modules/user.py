from dateutil import parser

from app.models import db, User


def registrate_user(data):
    """
    Registra o usuário de acordo com os dados validados na requisição.
    TODO: adicionar parser para a data de nascimento.
    """
    usr = User(**data)
    data['birthdate'] = parser.parse(data['birthdate'])
    db.session.add(usr)
    db.session.commit()
