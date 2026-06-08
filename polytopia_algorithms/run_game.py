import random

from polytopia_game.settings import Settings
from game_runner import Game

# Players
maximalizalo_jatekos = "Player 1 (Max)"
minimalizalo_jatekos = "Player 2 (Min)"

# Game tree (scores at the leaf nodes)
tree = [None, None, None, None, None, None, None, 5, 6, 7, 1, -13, 9, -8, -4]

map_settings = {
    "game_mode": Settings.GAME_MODE,
    "map_size": Settings.MAP_SIZE,
    "map_type": Settings.MAP_TYPE.name,
}

players = ['Zoy', 'Midjiwan']
game = Game(maximalizalo_jatekos, minimalizalo_jatekos, tree, map_settings, players)

(player_scores, minmax_score) = game.run()
winner = maximalizalo_jatekos if minmax_score > 0 else minimalizalo_jatekos

print(f"Players: {game.players}")
print(f"Player names: {game.player_names}")
print(f"Length of player names: {len(game.player_names)}")
print(f"Player scores: {player_scores}")


if game.player_names:
    winner = random.choice([game.player_names[0], game.player_names[-1]])
else:
    winner = "Unknown"  # or any other default behavior
print(f"The winner is: {winner}! Personal score: {player_scores}. Game score: {minmax_score}")
