import typing
from dataclasses import dataclass, field


@dataclass
class Match():
    id_: str = None
    player_names: typing.List[str] = field(default_factory=lambda: [0, 0])
    player_sets: typing.List[int] = field(default_factory=lambda: [0, 0])

    def report(self):
        winning_player = self.player_sets[1] > self.player_sets[0]
        loosing_player = not winning_player

        return f"{self.player_names[winning_player]} defeated {self.player_names[loosing_player]}\n{self.player_sets[winning_player]} sets to {self.player_sets[loosing_player]}"


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

    def report(self) -> str:
        memo = [m.report() for m in self.matches.values()]
        memo.append("")
        memo += [f"{player.name} stats: {player.report()}" for player in self.players.values()]
        return memo
