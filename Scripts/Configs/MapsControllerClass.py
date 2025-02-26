import pygame
from Scripts.ClassesObjects.MapClass import Map

class MapsController:
    def __init__(self, width, height):
        self.__tile_scale = height * 0.1
        self.__gasps_scale = self.__tile_scale * 0.2
        self.__trajectory = ()
        self.__level = 0
        self.__map_array = [Map([[0, 8, 1, 1, 1],
                                 [1, 0, 0, 0, 0],
                                 [2, 0, 3, 0, 3],
                                 [0, 0, 0, 0, 2],
                                 [1, 0, 1, 0, 1]],
                                [[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4)], [0, 1, 1, 0, 0, 3, 3, 0]], width, height, self.__tile_scale),
                            Map([[1, 0, 0, 0, 1],
                    [1, 2, 1, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 4, 0],
                    [0, 1, 3, 0, 0]],
                              [[(0, 4), (0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)],
                    [0, 0, 3, 3, 3, 0, 0, 1, 1, 1]], width, height, self.__tile_scale),
                            Map([[0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 1, 4, 0, 0, 1],
                    [0, 5, 2, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 3, 0],
                    [1, 0, 0, 0, 1, 0, 0]],
                              [[(0, 3), (5, 1), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 3)], [3, 0, 3, 0, 3, 0, 0, 3, 3, 2]], width, height, self.__tile_scale),
                            Map([[0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 3, 0],
                    [1, 0, 7, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 1],
                    [5, 0, 4, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 2, 0, 0, 0]],
                              [[(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2)], [2, 1, 2, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 2]], width, height, self.__tile_scale),
                            Map([[0, 0, 0, 0, 1, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 5],
                    [1, 0, 1, 7, 0, 0, 1],
                    [2, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 3, 4, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0]],
                              [[(6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4)], [1, 0, 0, 0, 0, 1, 1, 2, 1, 1, 2, 2, 2]], width, height, self.__tile_scale),
                            Map([[0, 0, 1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 3, 0, 4, 0, 1],
                    [0, 1, 0, 5, 0, 0, 2],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 7, 0, 0]], [[(2, 6), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)], [0, 3, 3, 3, 0, 0, 0, 0, 1, 1, 1, 1, 2]], width, height, self.__tile_scale)]

    def fail_map(self, time):
        self.__map_array[int(self.__level) - 1].destruct_base(time)

    def change_level(self, new_value):
        self.__level = new_value

    def draw_map(self, context):
        self.__map_array[int(self.__level) - 1].draw(context)

    def get_tile_scale(self):
        return self.__tile_scale

    def get_build_array(self):
        return self.__map_array[int(self.__level) - 1].build_array

    def get_started_position(self, position_enemy_on_tile):
        return self.__map_array[int(self.__level) - 1].get_started_position(position_enemy_on_tile)

    def update_trajectory_array(self):
        self.__trajectory =  self.__map_array[int(self.__level) - 1].get_trajectory_array()

    def get_trajectory(self):
        return self.__trajectory

    def definition_current_tile(self, event, context):
        mouse_pose = pygame.mouse.get_pos()  # получает позицию мышки
        context.get_config_gameplay().set_highlight_tile(None)
        if context.get_config_parameter_scene().get_width() - context.get_config_parameter_scene().get_height() * 0.4 > mouse_pose[0] > context.get_config_parameter_scene().get_height() * 0.4:
            tile_scale = context.get_config_parameter_scene().get_tile_scale()
            build_array = self.get_build_array()
            for i in range(
                    len(build_array)):  # Проходит по координатам всех тайлов, и если они совпадут с координатой мышки, то этот тайл сохранится как текущий тайл. Если мышка была нажата, та как действующий тайл
                if build_array[i]['coordinate'][0] <= mouse_pose[0] <= build_array[i]['coordinate'][0] + tile_scale and build_array[i]['coordinate'][1] <= mouse_pose[1] <= \
                        build_array[i]['coordinate'][1] + tile_scale:
                    context.get_config_gameplay().set_highlight_tile(i)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        context.get_config_gameplay().set_current_tile(i)
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    context.get_config_gameplay().set_current_tile(None)