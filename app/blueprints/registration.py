from flask import Blueprint, request, jsonify
from app.modules.user import registrate_user

bp = Blueprint('registration', __name__)


@bp.route('/sign_up', methods=['POST'])
def sign_up():
    if not request.json:
        return jsonify(message='Error: this route only accepts json')
    
    registrate_user(request.json)
    return jsonify(message='success'), 201
