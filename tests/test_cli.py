import argparse
import os
import io

from scorer import cli


def test_cli(capsys, monkeypatch):
    fp = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'data',
        'full_tournament.txt'
    )

    queries = io.StringIO("Score Match 02\nGames Player Person A\n")
    monkeypatch.setattr('sys.stdin', queries)
    namespace = argparse.Namespace(file_path=fp, debug=False)

    cli.run_cli(namespace)
    captured = capsys.readouterr()
    expected = '''
Person C defeated Person A
2 sets to 1

23 17

'''
    assert captured.out == expected


def test_cli_debug(capsys, monkeypatch):
    fp = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'data',
        'full_tournament.txt'
    )

    namespace = argparse.Namespace(file_path=fp, debug=True)
    cli.run_cli(namespace)
    captured = capsys.readouterr()
    expected = '''Person A defeated Person B
2 sets to 0
Person C defeated Person A
2 sets to 1

Person A stats: 23 17
Person B stats: 0 12
Person C stats: 17 11
'''
    assert captured.out == expected
