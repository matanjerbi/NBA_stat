from db_con import db



class PlayerStats(db.Model):  # Inherit from db.Model
    __tablename__ = 'player_stats'

    #data from the API
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String, nullable=True)
    position = db.Column(db.String, nullable=True)
    games = db.Column(db.Integer, nullable=True)
    field_goals = db.Column(db.Integer, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    two_percent = db.Column(db.Float, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    team = db.Column(db.String, nullable=True)
    season = db.Column(db.Integer, nullable=True)
    player_id = db.Column(db.String, nullable=True)

    #data from our calculations
    atr = db.Column(db.Float, nullable=True)
    ppg_ratio = db.Column(db.Float, nullable=True)

    # serialize the data



    def __repr__(self):
        return (f"<PlayerStats(player_name={self.player_name}, team={self.team},"
                f" season={self.season})>")

    def to_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'position': self.position,
            'games': self.games,
            'field_goals': self.field_goals,
            'three_percent': self.three_percent,
            'two_percent': self.two_percent,
            'assists': self.assists,
            'turnovers': self.turnovers,
            'points': self.points,
            'team': self.team,
            'season': self.season,
            'player_id': self.player_id,
            'atr': self.atr,
            'ppg_ratio': self.ppg_ratio
        }

if __name__ == "__main__":
    db.create_all()

    # player = PlayerStats(id=18127, player_name="Jalen Crutcher", position="PG", games=1, field_goals=0,
    #                      three_percent=None, two_percent=0.000, assists=0, turnovers=0,
    #                      points=0, team="NOP", season=2024, player_id="crutcja01")
    #
    # db.session.add(player)
    # db.session.commit()
