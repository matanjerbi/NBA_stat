import requests
from models.players import PlayerStats
from db_con import db

def get_players_for_one_season(year):
    NBA_url = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{year}'

    dict_lst = []
    try:
        response = requests.get(NBA_url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    all_posisions_ppg = calc_all_position_ppg(data)

    for player in data:
        player_id = player['playerId']
        player_name = player['playerName']
        position = player['position']
        games = player['games']
        field_goals = player.get('fieldGoals', 0)
        three_percent = player.get('threePercent', 0.0)
        two_percent = player.get('twoPercent', 0.0)
        assists = player.get('assists', 0)
        turnovers = player.get('turnovers', 0)
        points = player.get('points', 0)
        team = player['team']
        season = player['season']

        player_dict = {
            'player_id': player_id,
            'player_name': player_name,
            'position': position,
            'games': games,
            'field_goals': field_goals,
            'three_percent': three_percent,
            'two_percent': two_percent,
            'assists': assists,
            'turnovers': turnovers,
            'points': points,
            'team': team,
            'season': season,
            'atr': calculate_atr(player),
            'ppg': calc_ppg_per_player(player, all_posisions_ppg)
        }
        dict_lst.append(player_dict)

        player_stats = PlayerStats(
            player_id=player_id,
            player_name=player_name,
            position=position,
            games=games,
            field_goals=field_goals,
            three_percent=three_percent,
            two_percent=two_percent,
            assists=assists,
            turnovers=turnovers,
            points=points,
            team=team,
            season=season,
            atr=player_dict['atr'],
            ppg_ratio=player_dict['ppg']
        )
        print(f"Successfully saved player {player_name} to the database.")
        db.session.add(player_stats)

    db.session.commit()

    return dict_lst

def get_players_for_all_seasons():
    seasons = [2022, 2023, 2024]
    for year in seasons:
        get_players_for_one_season(year)
    return "All players have been successfully fetched and saved to the database."



def calculate_atr(player_dict) -> float:
    return player_dict['assists'] / player_dict['turnovers'] if player_dict['turnovers'] != 0 else 0


def calc_ppg_by_position(lst_players, position):
    points = 0
    games = 0
    for player in lst_players:
        if player['position'] == position:
            points += player['points']
            games += player['games']
    return points / games if games != 0 else 0


def calc_all_position_ppg(all_players: list) -> dict:
    ppg_ratio = {}
    for position in ['PG', 'SG', 'SF', 'PF', 'C']:
        ppg_ratio[position] = calc_ppg_by_position(all_players, position)
    return ppg_ratio


def calc_ppg_per_player(player: dict, average_per_position: dict) -> float:
    if player['games'] == 0:
        return 0
    return player['points'] / player['games'] / average_per_position.get(player['position'], 1)
