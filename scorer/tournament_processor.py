import typing
import io

from data_objects import Match, Player, Tournament

MATCH_ID_PREAMBLE = 'Match: '
MINIMUM_POINTS_TO_WIN_GAME = 4
POINTS_LEAD_TO_WIN_GAME = 2
GAMES_TO_WIN_SET = 6
SETS_TO_WIN = 2


def gameConcluded(player1_points: int, player2_points: int) -> bool:
    if player1_points < MINIMUM_POINTS_TO_WIN_GAME and player2_points < MINIMUM_POINTS_TO_WIN_GAME:
        return False

    return abs(player1_points - player2_points) >= POINTS_LEAD_TO_WIN_GAME


def matchConcluded(player1_sets: int, player2_sets: int) -> bool:
    return player1_sets == SETS_TO_WIN or player2_sets == SETS_TO_WIN


def updatePlayerTotalGames(a_name: str, a_games_won: int, b_name: str, b_games_won: int, t: Tournament):
    if a_name in t.players.keys():
        t.players[a_name].won_games += a_games_won
        t.players[a_name].lost_games += b_games_won
    else:
        t.players[a_name] = Player(
            a_name, a_games_won, b_games_won)

    if b_name in t.players.keys():
        t.players[b_name].won_games += b_games_won
        t.players[b_name].lost_games += a_games_won
    else:
        t.players[b_name] = Player(
            b_name, b_games_won, a_games_won)


def ProcessTournament(fh: typing.TextIO) -> Match:
    tournament = Tournament()
    player1_points = 0
    player2_points = 0
    player1_games_for_set = 0
    player2_games_for_set = 0
    match: Match = None

    for line in fh.readlines():
        if len(line.strip()) == 0:
            continue

        if line.startswith(MATCH_ID_PREAMBLE):
            if match is not None:
                tournament.matches[match.id_] = match
                updatePlayerTotalGames(match.player1_name, player1_games_for_set,
                                       match.player2_name, player2_games_for_set, tournament)

            match = Match()
            match.id_ = line.split(MATCH_ID_PREAMBLE)[1].strip()
            print(f"found match {match}")
            player1_points = 0
            player2_points = 0
            player1_games_for_set = 0
            player2_games_for_set = 0
            continue

        if " vs " in line:
            player_names = line.split(" vs ")
            print(f"player_names {player_names}")
            match.player1_name = player_names[0]
            match.player2_name = player_names[1].strip()

        if line == "0\n":
            print("player 1 pt")
            player1_points += 1

        if line == "1\n":
            player2_points += 1

        if gameConcluded(player1_points, player2_points):
            print("game")
            if player1_points > player2_points:
                player1_games_for_set += 1
            else:
                player2_games_for_set += 1

            player1_points = 0
            player2_points = 0

            if player1_games_for_set == GAMES_TO_WIN_SET or player2_games_for_set == GAMES_TO_WIN_SET:
                print("set")
                if player1_games_for_set > player2_games_for_set:
                    print("a")
                    match.player1_sets += 1
                else:
                    print("b")
                    match.player2_sets += 1

                updatePlayerTotalGames(match.player1_name, player1_games_for_set,
                                       match.player2_name, player2_games_for_set, tournament)

                player1_games_for_set = 0
                player2_games_for_set = 0
                print(f"x\n{match}\nx")

                if matchConcluded(match.player1_sets, match.player2_sets):
                    print('end of match')
                    tournament.matches[match.id_] = match

                    match = None

    return tournament
