import argparse
import sys
from pprint import pprint

from .tournament_processor import process_tournament
from .query_processor import process_queries


def create_argparser():
    parser = argparse.ArgumentParser(
        description="Estimate One tennis tournament coding challenge"
    )
    parser.add_argument('file_path', type=str,
                        help="Path to tournament data")
    parser.add_argument(
        'queries', type=str, help="Queries to run against data, e.g. 'Games Player x' or 'Score Match y'", nargs="?")
    return parser


def run_cli():
    parser = create_argparser()
    args = parser.parse_args()

    with open(args.file_path, "rt") as fh:
        data = process_tournament(fh)

    if args.queries is None:
        answers = data.report()
    else:
        answers = process_queries()

    print("\n".join(answers))
