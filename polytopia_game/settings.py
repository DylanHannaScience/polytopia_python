import random
import pathlib
from enum import Enum

class GameMode(Enum):
    GLORY = 0
    MIGHT = 1
    FREE_ROAMING_MODE = 2  # FNAF reference

class MapSizes(Enum):
    TINY = 11
    SMALL = 14
    NORMAL = 16
    LARGE = 18
    HUGE = 20
    MASSIVE = 30

    def __mul__(self, other):
        if isinstance(other, (int, float)):  # Multiply with numbers
            return self.value * other
        elif isinstance(other, MapSizes):  # Multiply with another enum member
            return self.value * other.value
        else:
            raise TypeError(f"Unsupported operand type(s) for *: '{type(self)}' and '{type(other)}'")

class MapTypes(Enum):
    DRYLAND = 0
    LAKES = 1
    PANGEA = 2
    CONTINENTS = 3
    ARCHIPELAGO = 4
    WATER_WORLD = 5


def setNumberOfPlayers(number_of_desired_players):
    if number_of_desired_players < 2:
        raise ValueError("The number of players must be at least 2!")
    if number_of_desired_players > 16:
        raise ValueError("There cannot be more than 16 players in a game!")
    return number_of_desired_players


class Settings:
    GAME_MODE = GameMode.MIGHT

    MAP_HEIGHT = MapSizes.NORMAL
    MAP_WIDTH = MapSizes.NORMAL

    MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

    MAP_TYPE = MapTypes.DRYLAND

    NUMBER_OF_PLAYERS = setNumberOfPlayers(2)


    TILE_PROPERTY_CHANNEL = 0
    UNIT_TYPE_CHANNEL = 1
    UNIT_STATE_CHANNEL = 2
    UNIT_TEAM_CHANNEL = 3
    UNIT_HEALTH_CHANNEL = 4

    CHANNEL_ATTRIBUTES = {0: {"channel name": "tile property",
                              "description": """
                              What 'property' is on the tile, such as a resource type (forest, animal, etc.).
                              Needed for the V0 example because a tile can either have nothing on it, or a 
                              city.
                              """,
                              "possible values": {0: "nothing",
                                                  1: "team 1 city",
                                                  2: "team 2 city"}},
                           1: {"channel name": "unit type",
                               "description": """
                               The kind of unit that is on the tile (warrior, rider, etc.). Even though V0
                               will feature warriors as the only unit, this channel is necessary to 
                               highlight the *absence* of a unit.
                               """,
                               "possible values": {0: "no unit",
                                                   1: "warrior"}},
                           2: {"channel name": "unit state",
                               "description": """
                               What 'state' that unit is currently in. Examples include unit being able to 
                               move/attack, being able to just attack, or being able to just move. This will
                               mostly be necessary for V0 to distinguish between units that have already moved
                               in this turn, or those that can still move.
                               """,
                               "possible values": {0: "unit has not taken action",
                                                   1: "unit has moved, but can still attack",
                                                   2: "unit can no longer take action"}},
                           3: {"channel name": "unit team",
                               "description": """
                               What team the unit is on. In V0 there will only be two possible teams. This is 
                               separate from the concept of a 'tribe', which is absent in V0.
                               """,
                               "possible values": {0: "no team",
                                                   1: "team 1",
                                                   2: "team 2"}},
                          4: {"channel name": "unit health",
                              "description": """
                              How much health the unit has remaining. This is an int value (instead of a 
                              category). The maximum possible health value in V0 would be 15 (for a veteran
                              warrior), and the minimum would be 1.
                              """,
                              "possible values": {0: "no unit",
                                                  1-15: "unit health value"}}
                          }

    ## OTHER THINGS THAT NEED TO BE TRACKED FOR THE GAME STATE:
    # - Current player team (0/1)
    # - Number of Stars
    # - Number of units (0-2)
    # - Score of players

    BASE_DIR = str(pathlib.Path(__file__).parent.resolve())