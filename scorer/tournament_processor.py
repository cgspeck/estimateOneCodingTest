import typing
import io

from .data_objects import Match, Player, Tournament

MATCH_ID_PREAMBLE = 'Match: '
MINIMUM_POINTS_TO_WIN_GAME = 4
POINTS_LEAD_TO_WIN_GAME = 2
GAMES_TO_WIN_SET = 6
SETS_TO_WIN = 2
VALID_SCORING_LINES = ["0\n", "1\n"]


def gameConcluded(player_points: typing.List[int]) -> bool:
    if all([score < MINIMUM_POINTS_TO_WIN_GAME for score in player_points]):
        return False

    return abs(player_points[0] - player_points[1]) >= POINTS_LEAD_TO_WIN_GAME


def matchConcluded(match: Match) -> bool:
    return any([x == SETS_TO_WIN for x in match.player_sets])


def updatePlayerTotalGames(match: Match, games_for_set: typing.List[int], t: Tournament):
    for idx, player_name in enumerate(match.player_names):
        won_games_this_set = games_for_set[idx]
        lost_games_this_set = games_for_set[not idx]

        if player_name in t.players.keys():
            t.players[player_name].won_games += won_games_this_set
            t.players[player_name].lost_games += lost_games_this_set
        else:
            t.players[player_name] = Player(
                player_name, won_games_this_set, lost_games_this_set)


def process_tournament(fh: typing.TextIO) -> Match:
    tournament = Tournament()
    player_points = [0, 0]
    games_for_set = [0, 0]
    match: Match = None

    for line in fh.readlines():
        if len(line.strip()) == 0:
            continue

        if line.startswith(MATCH_ID_PREAMBLE):
            if match is not None:
                tournament.matches[match.id_] = match
                updatePlayerTotalGames(match, games_for_set, tournament)

            match = Match()
            match.id_ = line.split(MATCH_ID_PREAMBLE)[1].strip()
            player_points = [0, 0]
            games_for_set = [0, 0]
            continue

        if " vs " in line:
            match.player_names = line.strip().split(" vs ")

        if any(scoring_line in line for scoring_line in VALID_SCORING_LINES):
            player_points[int(line)] += 1

        if gameConcluded(player_points):
            idx_to_update = player_points[1] > player_points[0]
            games_for_set[idx_to_update] += 1

            player_points = [0, 0]

            if games_for_set[0] == GAMES_TO_WIN_SET or games_for_set[1] == GAMES_TO_WIN_SET:
                idx_to_update = games_for_set[1] > games_for_set[0]
                match.player_sets[idx_to_update] += 1

                updatePlayerTotalGames(match, games_for_set, tournament)

                games_for_set = [0, 0]

                if matchConcluded(match):
                    tournament.matches[match.id_] = match

                    match = None

    return tournament
