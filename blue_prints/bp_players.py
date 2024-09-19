from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from markupsafe import escape
from models.players import PlayerStats, db
from services.read_from_api_NBA import get_players_for_all_seasons
from services.read_from_api_NBA import get_players_for_one_season
from services.get_players import get_players_by_position


player_bp = Blueprint('players', __name__, url_prefix='/api/players')


# @player_bp.route('/', methods=['GET'])
# def get_players_for_all_seasons():
#     print("Fetching players for all seasons...")
#     all_players = PlayerStats.query.all()
#     players_json = [player.to_json() for player in all_players]
#     return jsonify(players_json)


years = [2022, 2023, 2024]
@player_bp.route('/', methods=['GET'])
def home():
    try:
        for year in years:
            get_players_for_one_season(year)
        return jsonify({'message': 'Database created successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@player_bp.route('/all', methods=['GET'])
def get_players():
    all_players = PlayerStats.query.all()
    players_json = [player.to_dict() for player in all_players]
    return jsonify(players_json)


@player_bp.route('/position', methods=['GET'])
def get_players_by_position():
    position = request.args.get('position')
    if not position:
        return jsonify({"error": "Position is required"}), 400
    players = get_players_by_position(position)
    return players


@player_bp.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Resource not found"}), 404











