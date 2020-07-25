import io

from scorer.data_objects import Match, Player, Tournament
from scorer.query_processor import process_queries


def test_process_query():
    tournament = Tournament(
        matches={
            '01': Match(id_='01', player_names=['Person A', 'Person B'], player_sets=[2, 0]),
            '02': Match(id_='02', player_names=['Person A', 'Person C'], player_sets=[1, 2])
        },
        players={
            'Person A': Player(name='Person A', won_games=23, lost_games=17),
            'Person B': Player(name='Person B', won_games=0, lost_games=12),
            'Person C': Player(name='Person C', won_games=17, lost_games=11)
        }
    )

    expected = ['Person C defeated Person A\n2 sets to 1', '23 17']
    queries = io.StringIO("Score Match 02\nGames Player Person A\n")
    assert process_queries(queries, tournament) == expected


def test_process_query_blank_line_option():
    tournament = Tournament(
        matches={
            '01': Match(id_='01', player_names=['Person A', 'Person B'], player_sets=[2, 0]),
            '02': Match(id_='02', player_names=['Person A', 'Person C'], player_sets=[1, 2])
        },
        players={
            'Person A': Player(name='Person A', won_games=23, lost_games=17),
            'Person B': Player(name='Person B', won_games=0, lost_games=12),
            'Person C': Player(name='Person C', won_games=17, lost_games=11)
        }
    )

    expected = ['Person C defeated Person A\n2 sets to 1', '', '23 17', '']
    queries = io.StringIO("Score Match 02\nGames Player Person A\n")
    assert process_queries(queries, tournament, blank_line=True) == expected
