from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from markupsafe import escape
from models.players import PlayerStats, db
from services.read_from_api_NBA import get_player

player_bp = Blueprint('players', __name__, url_prefix='/api/players')


@player_bp.route('/', methods=['GET'])
def get_players():
    get_player()
    players = PlayerStats.query.all()
    return jsonify([player.serialize for player in players])


@player_bp.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404











