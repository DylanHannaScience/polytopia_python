

# Local
from game_map import GameMap
import settings

MAP_HEIGHT = settings.MAP_HEIGHT
MAP_WIDTH = settings.MAP_WIDTH

class GameSimulator:
    def __init__(self):
        self.game_map = GameMap()
        self.game_map.generate_map()


