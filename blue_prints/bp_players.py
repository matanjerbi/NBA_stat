from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from markupsafe import escape
from models.players import PlayerStats, db
from services.read_from_api_NBA import get_players_for_all_seasons

player_bp = Blueprint('players', __name__, url_prefix='/api/players')


@player_bp.route('/', methods=['GET'])
def get_players_for_all_seasons():
    print("Fetching players for all seasons...")
    all_players = PlayerStats.query.all()
    players_json = [player.to_json() for player in all_players]
    return jsonify(players_json)


@player_bp.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404











