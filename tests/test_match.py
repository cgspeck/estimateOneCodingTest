import pytest

from scorer.data_objects import Match

EXPECTED_REPORT = "Person A defeated Person C\n2 sets to 1"


def test_match_report_player1_wins():
    match = Match(
        player_names=["Person A", "Person C"],
        player_sets=[2, 1]
    )

    assert match.report() == EXPECTED_REPORT


def test_match_report_player2_wins():
    # and when player two is the winner
    match = Match(
        player_names=["Person C", "Person A"],
        player_sets=[1, 2]
    )
    assert match.report() == EXPECTED_REPORT
