from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PlayerStats(db.Model):  # Inherit from db.Model
    __tablename__ = 'player_stats'

    player_name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    games = db.Column(db.Integer, nullable=False)
    field_goals = db.Column(db.Integer, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    two_percent = db.Column(db.Float, nullable=False)
    assists = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    team = db.Column(db.String, nullable=False)
    season = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return (f"<PlayerStats(player_name={self.player_name}, team={self.team},"
                f" season={self.season})>")


# Example code to add a player (assuming Flask app context):
if __name__ == "__main__":
    # Assuming this is run inside the Flask app context, e.g., with `app.app_context()`
    db.create_all()

    # Add a sample player (like Jalen Crutcher)
    player = PlayerStats(id=18127, player_name="Jalen Crutcher", position="PG", games=1, field_goals=0,
                         three_percent=None, two_percent=0.000, assists=0, turnovers=0,
                         points=0, team="NOP", season=2024, player_id="crutcja01")

    db.session.add(player)
    db.session.commit()
