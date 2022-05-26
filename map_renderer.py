# Standard Python
import copy
import os

# Third-party
import numpy as np
from PIL import Image

# Local
import settings

MAP_HEIGHT = settings.MAP_HEIGHT
MAP_WIDTH = settings.MAP_WIDTH

tile_x_modifier = 37
tile_y_modifier = 22


class MapRenderer:

    def render_map(self, city_config_list):
        rendered_map_img = self.render_terrain_tiles()
        self.add_cities_to_map(rendered_map_img, city_config_list)

        rendered_map_img.save(os.path.join(settings.BASE_DIR, "rendered_images/rendered_map.png"))


    def render_terrain_tiles(self):
        grass_tile_img = self.load_grass_tile_img()
        grass_tile_array = np.array(grass_tile_img)

        self.tile_height, self.tile_width = grass_tile_array.shape[:2]

        rendered_map_array = self.get_empty_map_array()
        map_x_midpoint = rendered_map_array.shape[1]//2
        rendered_map_img = Image.fromarray(rendered_map_array)

        self.starting_tile_position_y = 0
        self.starting_tile_position_x = map_x_midpoint - tile_x_modifier

        for column in range(0, MAP_WIDTH):
            for row in range(0, MAP_HEIGHT):

                map_array_with_tile = copy.deepcopy(rendered_map_array)

                tile_y_start_coord, tile_y_end_coord = self.get_tile_y_coordinates(row, column)
                tile_x_start_coord, tile_x_end_coord = self.get_tile_x_coordinates(row, column)

                map_array_with_tile[tile_y_start_coord:tile_y_end_coord,
                                    tile_x_start_coord:tile_x_end_coord,
                                    :] = grass_tile_array
                rendered_tile_in_map_space = Image.fromarray(map_array_with_tile)
                rendered_map_img.alpha_composite(rendered_tile_in_map_space)

        return rendered_map_img

    @staticmethod
    def load_grass_tile_img():
        grass_tile_img = Image.open(os.path.join(settings.BASE_DIR, "image_assets/Grass.webp"))

        return grass_tile_img

    @staticmethod
    def load_city_img(team_colour):
        city_img = Image.open(os.path.join(settings.BASE_DIR, f"image_assets/{team_colour}_team_city.png"))

        return city_img

    def get_rendered_map_dimensions(self):
        rendered_map_height = (MAP_HEIGHT*2 - 2)*tile_y_modifier + self.tile_height
        rendered_map_width = MAP_WIDTH*self.tile_width
        rendered_map_channels = 4

        return (rendered_map_height, rendered_map_width, rendered_map_channels)

    def get_tile_y_coordinates(self, row, column):

        tile_y_start_coord = self.starting_tile_position_y+(tile_y_modifier*(row+column))
        tile_y_end_coord = self.starting_tile_position_y+(tile_y_modifier*(row+column))+self.tile_height

        return tile_y_start_coord, tile_y_end_coord

    def get_tile_x_coordinates(self, row, column):

        tile_x_start_coord = self.starting_tile_position_x+(tile_x_modifier*(column-row))
        tile_x_end_coord = self.starting_tile_position_x+(tile_x_modifier*(column-row))+self.tile_width

        return tile_x_start_coord, tile_x_end_coord

    def add_cities_to_map(self, rendered_map_img, city_config_list):

        for city_config in city_config_list:

            city_img = self.load_city_img(team_colour=city_config['team_colour'])

            row, column = city_config['row'], city_config['column']

            # row indexes don't neatly align with tile conception of "row" and "column"
            geometric_row, geometric_column = self.convert_array_indexes_to_geometric_indexes(row, column)

            # Subtracting one from row and column to account for large sizes of city imgs
            city_y_start_coord, _ = self.get_tile_y_coordinates(row=geometric_row-1, column=geometric_column-1)
            city_x_start_coord, _ = self.get_tile_x_coordinates(row=geometric_row-1, column=geometric_column-1)

            city_height, city_width, _ = np.array(city_img).shape

            empty_map_array_with_city = self.get_empty_map_array()

            empty_map_array_with_city[city_y_start_coord:city_y_start_coord+city_height,
                                      city_x_start_coord:city_x_start_coord+city_width,
                                      :] = city_img

            rendered_city_in_map_space = Image.fromarray(empty_map_array_with_city)
            rendered_map_img.alpha_composite(rendered_city_in_map_space)

    def get_empty_map_array(self):
        return np.zeros(shape=self.get_rendered_map_dimensions(),
                        dtype=np.uint8)

    @staticmethod
    def convert_array_indexes_to_geometric_indexes(row, column):
        geometric_row = 5-column
        geometric_column = row

        return geometric_row, geometric_column


city_config_list = [{'team_colour': 'red',
                     'row': 1,
                     'column': 3},
                    {'team_colour': 'blue',
                     'row': 3,
                     'column': 5}]

map_renderer = MapRenderer()
map_renderer.render_map(city_config_list)