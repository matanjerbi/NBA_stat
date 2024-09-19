from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from markupsafe import escape
from models.players import PlayerStats, db

fantasy_bp = Blueprint('team', __name__, url_prefix='api/team')
