from scorer.data_objects import Match, Player, Tournament


def test_tournament_report():
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

    expected = [
        'Person A defeated Person B\n2 sets to 0',
        'Person C defeated Person A\n2 sets to 1',
        '',
        'Person A stats: 23 17',
        'Person B stats: 0 12',
        'Person C stats: 17 11'
    ]

    assert expected == tournament.report()
