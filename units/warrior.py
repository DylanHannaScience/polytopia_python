import settings
import numpy as np

class Warrior: 
    def __init__(current_position: tuple[int, int]):
        self.health = 10
        self.unit_type = "warrior"
        self.max_movement_distance = 1
        self.attack_damage = 1
        self.defence = 1
        self.attack_range = 1
        self.current_position = current_position

    def move_char(movement_x: int, movement_y: int, map_state_array: np.ndarray):
        map_x, map_y = settings.MAP_WIDTH, settings.MAP_HEIGHT
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
        if map_state_array[new_position_y, new_position_x, settings.UNIT_TYPE_CHANNEL]:
            return

        # do the move
        # update
        