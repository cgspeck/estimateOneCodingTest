import argparse
import sys

from .tournament_processor import process_tournament
from .query_processor import process_queries


def create_parser():
    parser = argparse.ArgumentParser(
        description="Estimate One tennis tournament coding challenge"
    )
    parser.add_argument('file_path', type=str,
                        help="Path to tournament data")
    parser.add_argument(
        '--debug', '-d', action='store_true',
        help="Report on all Tournament data"
    )
    return parser


def run_cli(args):
    with open(args.file_path, "rt") as fh:
        data = process_tournament(fh)

    if args.debug:
        answers = data.report()
    else:
        answers = [""]
        answers += process_queries(sys.stdin, data, blank_line=True)

    print("\n".join(answers))


def main():
    args = create_parser().parse_args()
    run_cli(args)
