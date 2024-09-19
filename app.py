from flask import Flask, jsonify
from blue_prints.bp_players import player_bp
from blue_prints.bp_fantasy_group import fantasy_bp
from db_con import db
from services.read_from_api_NBA import get_players_for_all_seasons

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# init database
with app.app_context():
    db.create_all()

# initialize blueprints here
app.register_blueprint(player_bp)
app.register_blueprint(fantasy_bp)
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

@app.route('/')
def initialize_db():
    return jsonify(get_players_for_all_seasons())


if __name__ == '__main__':
    #function to read all players from API and save them to the database

    app.run(debug=True)


