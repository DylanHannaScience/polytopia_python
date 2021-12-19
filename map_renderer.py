# Standard Python
import copy

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

    def render_terrain_tiles(self):
        grass_tile_img = self.load_grass_tile_img()
        grass_tile_array = np.array(grass_tile_img)

        self.tile_height, self.tile_width = grass_tile_array.shape[:2]

        rendered_map_array = np.zeros(shape=self.get_rendered_map_dimensions(),
                                      dtype=np.uint8)
        map_x_midpoint = rendered_map_array.shape[1]//2
        rendered_map_img = Image.fromarray(rendered_map_array)

        self.starting_tile_position_y = 0
        self.starting_tile_position_x = map_x_midpoint - tile_x_modifier

        for column in range(0, MAP_WIDTH):
            for row in range(0, MAP_HEIGHT):

                map_array_with_tile = copy.deepcopy(rendered_map_array)

                tile_y_start_coord, tile_y_end_coord = self.get_tile_y_coordinates(row, column)
                tile_x_start_coord, tile_x_end_coord = self.get_tile_x_coordinates(row, column)


                map_array_with_tile[starting_tile_position_y+(tile_y_modifier*(row+column)):starting_tile_position_y+(tile_y_modifier*(row+column))+self.tile_height,
                map_start_x+(tile_x_modifier*(column-row)):map_start_x+(tile_x_modifier*(column-row))+tile_width,
                :] = grass_tile_array
                map_img_with_tile = Image.fromarray(map_array_with_tile)
                map_img.alpha_composite(map_img_with_tile)


    @staticmethod
    def load_grass_tile():
        grass_tile_img = Image.open("image_assets/Grass.webp")

        return grass_tile_img

    def get_rendered_map_dimensions(self):
        rendered_map_height = (MAP_HEIGHT*2 - 2)*tile_y_modifier + self.tile_height
        rendered_map_width = MAP_WIDTH*self.tile_width
        rendered_map_channels = 4

        return (rendered_map_height, rendered_map_width, rendered_map_channels)

    def get_tile_y_coordinates(self, row, column):

        tile_y_start_coord = self.starting_tile_position_y+(tile_y_modifier*(row+column))
        tile_y_end_coord = self.starting_tile_position_y+(tile_y_modifier*(row+column))+self.tile_height

        return tile_y_start_coord, tile_y_end_coord