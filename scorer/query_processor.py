import typing
import sys

from .data_objects import Tournament

VALID_QUERIES = [
    'games player',
    'score match'
]


def process_queries(queries: typing.TextIO, tournament: Tournament) -> typing.List[str]:
    memo = []

    for query_line in queries.readlines():
        stripped_query_line = query_line.strip()
        lower_query_line = stripped_query_line.lower()

        if not any([q in lower_query_line for q in VALID_QUERIES]):
            print(
                f"error: Unrecognized query '{stripped_query_line}'", file=sys.stderr)
            continue

        query_tokens = lower_query_line.split(" ")
        query = "_".join(query_tokens[0:2])

        arg_tokens = stripped_query_line.split(" ")
        arg = " ".join(arg_tokens[2:])

        memo.append(getattr(tournament, query)(arg))

    return memo
