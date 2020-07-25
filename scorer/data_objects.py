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

    def report(self):
        return f"{self.player1_name} defeated {self.player2_name}\n{self.player1_sets} sets to {self.player2_sets}"


@dataclass
class Player():
    name: str = None
    won_games: int = 0
    lost_games: int = 0

    def report(self):
        return f"{self.won_games} {self.lost_games}"


@dataclass
class Tournament():
    matches: typing.Dict[str, Match] = field(default_factory=dict)
    players: typing.Dict[str, Player] = field(default_factory=dict)

    def score_match(self, id_: str) -> str:
        pass

    def games_player(self, name: str) -> str:
        pass
