from db_con import db


class Team(db.Model):  # Inherit from db.Model
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, unique=True, nullable=False)
    player1_id = db.Column(db.string, nullable=False)
    playet2_id  = db.Column(db.String, nullable=False)
    player3_id = db.Column(db.String, nullable=False)
    player4_id = db.Column(db.String, nullable=False)
    player5_id = db.Column(db.String, nullable=False)

