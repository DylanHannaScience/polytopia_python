from typing import Any

from polytopia_game.settings import Settings
import random

class Game:
    def __init__(self, maximizing_player, minimizing_player, tree, map_settings, players):
        self.maximizing_player = maximizing_player
        self.minimizing_player = minimizing_player
        self.tree = tree
        self.map_settings = map_settings  # Currently unused, but can store game configuration.

        self.players = players
        self.player_names = ['Zoy', 'Midjiwan', 'Midjitone', 'GullYY', 'Espark', 'Tolbby', 'CadeTheFrogger', 'Innofunni',
                        'Finiite', 'Guardian', 'Generukk', 'McGoon', 'Sljivovica']
        random.shuffle(self.player_names)


    def run(self):
        print(f"Initialized players: {self.players}")

        # Shuffle player names
        random.shuffle(self.player_names)

        # Create player scores
        player_scores: dict[Any, int] = {}
        for player in self.players:
            player_scores[player] = random.randint(90, 1000) * 10 + 5

        # Random MinMax score
        minmax_score = random.randint(-100, 100)

        return player_scores, minmax_score