import typing
from dataclasses import dataclass, field


@dataclass
class Match():
    id_: str = None
    player1_name: str = None
    player1_sets: int = 0
    player1_games: int = 0
    player2_name: str = None
    player2_sets: int = 0
    player2_games: int = 0


@dataclass
class Player():
    name: str = None
    won_games: int = 0
    lost_games: int = 0


@dataclass
class Tournament():
    matches: typing.Dict[str, Match] = field(default_factory=dict)
    players: typing.Dict[str, Player] = field(default_factory=dict)

    def score_match(self, id_: str) -> str:
        pass

    def games_player(self, name: str) -> str:
        pass
