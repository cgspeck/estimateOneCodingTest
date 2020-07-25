from scorer.data_objects import Player


def test_player_report():
    expected_report = "23 17"
    player = Player(
        won_games=23,
        lost_games=17
    )
    assert player.report() == expected_report
