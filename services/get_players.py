from flask import jsonify

from db_con import db
from models.players import PlayerStats

def get_players_by_position(position):
    players = PlayerStats.query.filter_by(position=position)
    return jsonify([player.to_dict() for player in players])



