from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from markupsafe import escape
from users.models import PlayerStats, db

player_bp = Blueprint('users', __name__, url_prefix='/users')


@player_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = PlayerStats.query.get(user_id)
    if user:
        return jsonify(user.serialize())
    else:
        return jsonify({"error": "User not found"}), 404

@player_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = PlayerStats.query.get(user_id)
    if user:
        data = request.get_json()

        user.name = escape(data.get('name'))
        user.age = escape(data.get('age'))
        user.group = escape(data.get('group'))

        try:
            db.session.commit()
            return jsonify(user.serialize())
        except Exception as e:  # ��י��ו�� בכל ש��י��ה כללי��
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "User not found"}), 404


@player_bp.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404











