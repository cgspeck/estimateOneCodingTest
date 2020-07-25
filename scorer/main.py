import sys
from pprint import pprint

from . import tournament_processor


def run_cli():
    fp = sys.argv[1]
    with open(fp, "rt") as fh:
        res = tournament_processor.ProcessTournament(fh)
        pprint(res.matches)
        pprint(res.players)
