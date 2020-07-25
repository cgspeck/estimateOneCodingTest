import argparse
import sys
from pprint import pprint

from .tournament_processor import process_tournament
from .query_processor import process_queries


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Estimate One tennis tournament coding challenge"
    )
    parser.add_argument('file_path', type=str,
                        help="Path to tournament data")
    parser.add_argument(
        'queries', default=sys.stdin,
        help="Queries to run against data, e.g. 'Games Player x' or 'Score Match y'",
        nargs="?"
    )
    return parser.parse_args(argv)


def run_cli(argv):
    args = parse_args(argv)

    with open(args.file_path, "rt") as fh:
        data = process_tournament(fh)

    if args.queries is None:
        answers = data.report()
    else:
        answers = [""]
        answers += process_queries(args.queries, data, blank_line=True)

    print("\n".join(answers))


def main():
    run_cli(sys.argv[1:])
