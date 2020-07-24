from pprint import pprint
import tournament_processor

i = 0

with open("./data/full_tournament.txt", "rt") as fh:
    res = tournament_processor.ProcessTournament(fh)
    pprint(res.matches)
    pprint(res.players)
