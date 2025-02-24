from Map import Map

class MapsController:
    def __init__(self, width, height):
        self.tile_scale = height * 0.1
        self.gasps_scale = self.tile_scale * 0.2
        self.trajectory = ()
        self.level = 0
        self.map_array = [Map([[0, 8, 1, 1, 1],
                    [1, 0, 0, 0, 0],
                    [2, 0, 3, 0, 3],
                    [0, 0, 0, 0, 2],
                    [1, 0, 1, 0, 1]],
                    [[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4)], [0, 1, 1, 0, 0, 3, 3, 0]], width, height, self.tile_scale),
                    Map([[1, 0, 0, 0, 1],
                    [1, 2, 1, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 4, 0],
                    [0, 1, 3, 0, 0]],
                    [[(0, 4), (0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)],
                    [0, 0, 3, 3, 3, 0, 0, 1, 1, 1]], width, height, self.tile_scale),
                    Map([[0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 1, 4, 0, 0, 1],
                    [0, 5, 2, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 3, 0],
                    [1, 0, 0, 0, 1, 0, 0]],
                    [[(0, 3), (5, 1), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 3)], [3, 0, 3, 0, 3, 0, 0, 3, 3, 2]], width, height, self.tile_scale),
                    Map([[0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 3, 0],
                    [1, 0, 7, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1],
                    [5, 0, 4, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 2, 0, 0, 0]],
                    [[(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2)], [2, 1, 2, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 2]], width, height,self.tile_scale),
                    Map([[0, 0, 0, 0, 1, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 5],
                    [1, 0, 1, 7, 0, 0, 1],
                    [2, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 3, 4, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0]],
                    [[(6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4)], [1, 0, 0, 0, 0, 1, 1, 2, 1, 1, 2, 2, 2]], width, height, self.tile_scale),
                    Map([[0, 0, 1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 3, 0, 4, 0, 1],
                    [0, 1, 0, 5, 0, 0, 2],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 7, 0, 0]],[[(2, 6), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)], [0, 3, 3, 3, 0, 0, 0, 0, 1, 1, 1, 1, 2]], width, height, self.tile_scale)]

    def change_level(self, new_value):
        self.level = new_value

    def draw_map(self, context):
        self.map_array[int(self.level) - 1].draw(context)

    def get_tile_scale(self):
        return self.tile_scale

    def get_build_array(self):
        return self.map_array[int(self.level) - 1].build_array

    def get_started_position(self, position_enemy_on_tile):
        return self.map_array[int(self.level) - 1].get_started_position(position_enemy_on_tile)

    def update_trajectory_array(self):
        self.trajectory =  self.map_array[int(self.level) - 1].get_trajectory_array()

    def get_trajectory(self):
        return self.trajectory