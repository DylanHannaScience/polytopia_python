# Standard Python
import copy
import random

# Third-party
import numpy as np

# Local
import settings

MAP_HEIGHT = settings.MAP_HEIGHT
MAP_WIDTH = settings.MAP_WIDTH

TILE_PROPERTY_CHANNEL = settings.TILE_PROPERTY_CHANNEL
UNIT_TYPE_CHANNEL = settings.UNIT_TYPE_CHANNEL
UNIT_STATE_CHANNEL = settings.UNIT_STATE_CHANNEL
UNIT_TEAM_CHANNEL = settings.UNIT_TEAM_CHANNEL
UNIT_HEALTH_CHANNEL = settings.UNIT_HEALTH_CHANNEL


class GameMap:

    def __init__(self):
        self.first_city_indexes = ()
        self.second_city_indexes = ()

    def generate_map(self):
        self.map_state_array = np.zeros(shape=(MAP_HEIGHT, MAP_WIDTH, len(settings.CHANNEL_ATTRIBUTES)), dtype=np.uint8)
        self.add_cities_to_map()
        self.add_starting_units_to_map()

    def add_cities_to_map(self):

        city_boolean_mask = copy.deepcopy(self.map_state_array[:, :, 0]).astype(np.bool_)
        city_boolean_mask = self.assign_tiles_eligible_for_city_to_true(city_boolean_mask)

        eligible_tiles_for_first_city = self.get_eligible_tile_indexes(city_boolean_mask)
        self.first_city_indexes = random.choice(eligible_tiles_for_first_city)

        city_boolean_mask = self.assign_tiles_eligible_for_city_to_true(city_boolean_mask)
        eligible_tiles_for_second_city = self.get_eligible_tile_indexes(city_boolean_mask)
        self.second_city_indexes = random.choice(eligible_tiles_for_second_city)

        self.map_state_array[self.first_city_indexes + (TILE_PROPERTY_CHANNEL,)] = 1
        self.map_state_array[self.second_city_indexes + (TILE_PROPERTY_CHANNEL,)] = 2

    def assign_tiles_eligible_for_city_to_true(self, city_boolean_mask):

        if len(self.first_city_indexes) == 0:
            city_boolean_mask[1:MAP_HEIGHT-1, 1:MAP_WIDTH-1] = 1
        else:
            city_boolean_mask = self.set_tiles_too_close_to_first_city_to_false(city_boolean_mask,
                                                                                self.first_city_indexes)
        return city_boolean_mask

    @staticmethod
    def set_tiles_too_close_to_first_city_to_false(city_boolean_mask,
                                                   first_city_indexes):
        city_boolean_mask[max([first_city_indexes[0]-1, 0]):min([first_city_indexes[0]+1, MAP_WIDTH]),
                          max([first_city_indexes[1]-1, 0]):min([first_city_indexes[1]+1, MAP_HEIGHT])] = False

        return city_boolean_mask

    @staticmethod
    def get_eligible_tile_indexes(city_boolean_mask):

        row_column_index_arrays_for_eligible_tiles = np.where(city_boolean_mask)
        eligible_tile_indexes = [coordinate_tuple for coordinate_tuple in
                                 zip(row_column_index_arrays_for_eligible_tiles[0],
                                     row_column_index_arrays_for_eligible_tiles[1])]

        return eligible_tile_indexes

    def add_starting_units_to_map(self):
        self.map_state_array[self.first_city_indexes + (UNIT_TYPE_CHANNEL,)] = 1
        self.map_state_array[self.first_city_indexes + (UNIT_TEAM_CHANNEL,)] = 1
        self.map_state_array[self.first_city_indexes + (UNIT_HEALTH_CHANNEL,)] = 10
        self.map_state_array[self.first_city_indexes + (UNIT_STATE_CHANNEL,)] = 2

        self.map_state_array[self.second_city_indexes + (UNIT_TYPE_CHANNEL,)] = 1
        self.map_state_array[self.second_city_indexes + (UNIT_TEAM_CHANNEL,)] = 2
        self.map_state_array[self.second_city_indexes + (UNIT_HEALTH_CHANNEL,)] = 10
        self.map_state_array[self.second_city_indexes + (UNIT_STATE_CHANNEL,)] = 2


