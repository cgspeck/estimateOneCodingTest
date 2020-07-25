import pytest

from scorer.data_objects import Match

EXPECTED_REPORT = "Person A defeated Person C\n2 sets to 1"


def test_match_report_player1_wins():
    match = Match(
        player1_name="Person A",
        player1_sets=2,
        player2_name="Person C",
        player2_sets=1,
    )

    assert match.report() == EXPECTED_REPORT


@pytest.mark.xfail
def test_match_report_player2_wins():
    # and when player two is the winner
    match = Match(
        player1_name="Person C",
        player1_sets=1,
        player2_name="Person A",
        player2_sets=2,
    )
    assert match.report() == EXPECTED_REPORT
