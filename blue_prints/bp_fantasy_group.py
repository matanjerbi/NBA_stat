from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from markupsafe import escape
from models.players import PlayerStats, db
from services.validation_team import check_if_exsist

fantasy_bp = Blueprint('team', __name__, url_prefix='api/team')


@fantasy_bp.route('/', methods=['POST'])
def create_fantasy_group():
    try:
        data = request.get_json()
        check_if_exsist(data)
        new_group = PlayerStats(
            team_name=escape(data['team_name']),
            player_1=escape(data['player_1']),
            player_2=escape(data['player_2']),
            player_3=escape(data['player_3']),
            player_4=escape(data['player_4']),
            player_5=escape(data['player_5']),
        )
    except:
        return jsonify({"error": "Invalid data"}), 400