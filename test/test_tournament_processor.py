import os

from scorer.data_objects import Match, Player, Tournament
from scorer.tournament_processor import ProcessTournament


def test_full_tournament():
    fp = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'data',
        'full_tournament.txt'
    )

    expected_tournament = Tournament(
        matches={
            '01': Match(id_='01', player1_name='Person A', player1_sets=2, player1_games=0, player2_name='Person B', player2_sets=0, player2_games=0),
            '02': Match(id_='02', player1_name='Person A', player1_sets=1, player1_games=0, player2_name='Person C', player2_sets=2, player2_games=0)
        },
        players={
            'Person A': Player(name='Person A', won_games=23, lost_games=17),
            'Person B': Player(name='Person B', won_games=0, lost_games=12), 'Person C': Player(name='Person C', won_games=17, lost_games=11)
        }
    )
    with open(fp, "rt") as fh:
        actual_tournament = ProcessTournament(fh)

    assert expected_tournament == actual_tournament
