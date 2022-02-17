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

                map_array_with_tile[tile_y_start_coord:tile_y_end_coord,
                                    tile_x_start_coord:tile_x_end_coord,
                                    :] = grass_tile_array
                rendered_tile_in_map_space = Image.fromarray(map_array_with_tile)
                rendered_map_img.alpha_composite(rendered_tile_in_map_space)

        rendered_map_img.save(os.path.join(settings.BASE_DIR, "rendered_images/rendered_map.png"))


    @staticmethod
    def load_grass_tile_img():
        grass_tile_img = Image.open(os.path.join(settings.BASE_DIR, "image_assets/Grass.webp"))

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

    def get_tile_x_coordinates(self, row, column):

        tile_x_start_coord = self.starting_tile_position_x+(tile_x_modifier*(column-row))
        tile_x_end_coord = self.starting_tile_position_x+(tile_x_modifier*(column-row))+self.tile_width

        return tile_x_start_coord, tile_x_end_coord


map_renderer = MapRenderer()
map_renderer.render_terrain_tiles()