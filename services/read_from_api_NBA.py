import requests
from models.players import PlayerStats
from db_con import db

year_2022 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2022'
year_2023 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2023'
year_2024 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2024'
all_years = [year_2022, year_2023, year_2024]


def get_player():
    for year in all_years:
        response = requests.get(year)
        data = response.json()
        for player in data:
            player_id = player['PlayerID']
            player_name = player['PlayerName']
            position = player['Position']
            games = player['Games']
            field_goals = player['FieldGoals']
            three_percent = player['ThreePercent']
            two_percent = player['TwoPercent']
            assists = player['Assists']
            turnovers = player['Turnovers']
            points = player['Points']
            team = player['Team']
            season = player['Season']

            player_stats = PlayerStats(player_id=player_id, player_name=player_name, position=position, games=games,
                                     field_goals=field_goals, three_percent=three_percent, two_percent=two_percent,
                                     assists=assists, turnovers=turnovers, points=points, team=team, season=season)
            db.session.add(player_stats)
    db.session.commit()

