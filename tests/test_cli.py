import io
import os

from scorer import cli


def test_cli(capsys, monkeypatch):
    fp = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'data',
        'full_tournament.txt'
    )

    queries = io.StringIO("Score Match 02\nGames Player Person A\n")

    monkeypatch.setattr('sys.stdin', queries)
    cli.run_cli([fp])
    captured = capsys.readouterr()
    expected = '''
Person C defeated Person A
2 sets to 1

23 17

'''
    assert captured.out == expected
