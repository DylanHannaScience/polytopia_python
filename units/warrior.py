from settings import UNIT_TYPE_CHANNEL, UNIT_STATE_CHANNEL, UNIT_TEAM_CHANNEL,\
 UNIT_HEALTH_CHANNEL, UNIT_CHANNELS, UNIT_TYPES, MAP_HEIGHT, MAP_WIDTH
import numpy as np

class Warrior: 
    def __init__(self, current_position: tuple[int, int], team: int):
        self.health = 10
        self.unit_type = "warrior"
        self.max_movement_distance = 1
        self.attack_damage = 1
        self.defence = 1
        self.attack_range = 1
        self.current_position = current_position
        self.team = team

    def move_char(self, movement_x: int, movement_y: int, map_state_array: np.ndarray):
        map_x, map_y = MAP_WIDTH, MAP_HEIGHT
        current_x, current_y = self.current_position
        new_position_x = current_x + movement_x
        new_position_y = current_y + movement_y
        # make sure movement within movement range
        if movement_x > self.max_movement_distance or movement_y > self.max_movement_distance:
            return
        # make sure can't move off edge of map
        if (new_position_x > map_x or new_position_x < 0) or (new_position_x > map_y or new_position_y < 0):
            return 
        # make sure no other unit in the way
        if map_state_array[new_position_y, new_position_x, UNIT_TYPE_CHANNEL]:
            return

        # do the move
        map_state_array[new_position_y, new_position_x, UNIT_TYPE_CHANNEL] = UNIT_TYPES[self.unit_type]
        map_state_array[new_position_y, new_position_x, UNIT_STATE_CHANNEL] = 1
        map_state_array[new_position_y, new_position_x, UNIT_TEAM_CHANNEL] = self.team
        map_state_array[new_position_y, new_position_x, UNIT_HEALTH_CHANNEL] = self.health
        # removing state from old position of unit
        for UNIT_CHANNEL in UNIT_CHANNELS:
            map_state_array[current_y, current_x, UNIT_CHANNEL] = 0
        


        