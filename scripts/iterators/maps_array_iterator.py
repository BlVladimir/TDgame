from random import randrange

import pygame
from scripts.classes_objects.map_class import Map


class MapsArrayIterator:
    def __init__(self, width, height):
        if (width - 0.8 * height) / 1.2 <= height / 1.2:
            self.__tile_scale = (width - 0.8 * height) / 1.2
        else:
            self.__tile_scale = height / 1.2
        self.__trajectory = ()
        self.__level = 0
        self.__map_array = [Map([[0, 8, 1, 1, 1],
                               [1, 0, 0, 0, 0],
                               [2, 0, 3, 0, 3],
                               [0, 0, 0, 0, 2],
                               [1, 0, 1, 0, 1]],
                              [[(1, 4), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1)], [0, 1, 1, 0, 0, 3, 3, 0]], width, height, self.__tile_scale / 6),
                          Map([[8, 0, 0, 0, 1],
                               [1, 2, 1, 0, 1],
                               [0, 0, 0, 0, 0],
                               [0, 1, 0, 4, 0],
                               [0, 1, 3, 0, 0]],
                              [[(0, 4), (0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)],
                               [0, 0, 1, 1, 1, 0, 0, 3, 3, 3]], width, height, self.__tile_scale / 6),
                          Map([[0, 0, 0, 0, 0, 8, 0],
                               [0, 0, 1, 4, 0, 0, 1],
                               [0, 5, 2, 0, 0, 1, 0],
                               [0, 0, 1, 0, 0, 3, 0],
                               [1, 0, 0, 0, 1, 0, 0]],
                              [[(0, 3), (1, 3), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (4, 2), (4, 1), (5, 1)], [1, 2, 1, 1, 0, 0, 1, 0, 1, 0]], width, height, self.__tile_scale / 8),
                          Map([[0, 1, 0, 0, 0, 0, 0],
                               [1, 0, 0, 1, 1, 3, 0],
                               [1, 0, 1, 0, 0, 0, 0],
                               [0, 0, 0, 8, 0, 0, 1],
                               [5, 0, 4, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0, 1, 0],
                               [1, 0, 0, 2, 0, 0, 0]],
                              [[(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2)], [2, 3, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 3, 2]], width,
                              height, self.__tile_scale / 8),
                          Map([[0, 0, 0, 0, 1, 0, 0],
                               [1, 1, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 5],
                               [1, 0, 1, 6, 0, 0, 1],
                               [2, 0, 0, 0, 0, 0, 1],
                               [0, 8, 0, 3, 4, 0, 0],
                               [0, 0, 0, 0, 0, 1, 0]],
                              [[(6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4)], [3, 0, 0, 0, 0, 3, 3, 2, 3, 3, 2, 2, 2]], width, height,
                              self.__tile_scale / 8),
                          Map([[0, 0, 1, 0, 0, 1, 1],
                               [1, 0, 0, 0, 0, 0, 1],
                               [0, 8, 1, 0, 0, 0, 0],
                               [0, 0, 3, 0, 4, 0, 1],
                               [0, 1, 0, 5, 0, 0, 2],
                               [1, 0, 0, 0, 0, 0, 1],
                               [0, 1, 0, 0, 6, 0, 0]],
                              [[(2, 6), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)], [0, 1, 1, 1, 0, 0, 0, 0, 3, 3, 3, 3, 2]], width, height,
                              self.__tile_scale / 8)]

    def change_level(self, new_value):
        self.__level = new_value

    def draw_map(self, context):
        self.__map_array[int(self.__level) - 1].draw(context)

    def get_tile_scale(self):
        return self.__map_array[int(self.__level) - 1].get_tile_scale()

    def get_build_array(self):
        return self.__map_array[int(self.__level) - 1].get_build_array()

    def get_started_position(self, position_enemy_on_tile):
        return self.__map_array[int(self.__level) - 1].get_started_position(position_enemy_on_tile)

    def update_trajectory_array(self):
        self.__trajectory =  self.__map_array[int(self.__level) - 1].get_trajectory_array()

    def get_trajectory(self):
        return self.__trajectory

    def get_started_angle(self):
        return self.__map_array[int(self.__level) - 1].get_started_angel()

    def __get_level_of_enemies(self):
        if int(self.__level) <= 3:
            return int(self.__level) + 1
        else:
            return 4

    def create_waves(self, number_of_waves, context):  # Функция создает массив заданной длины, состоящий из 1, 2 и 3. Нужен для определения количества врагов на каждой волне
        waves_array = [[]]
        level_of_enemies = self.__get_level_of_enemies()
        for i in range(number_of_waves):
            waves_array[i].append(randrange(1, 4))
            waves_array[i].append(randrange(0, level_of_enemies))
            if i != number_of_waves - 1:
                waves_array.append([])
        waves_array[0][1] = 0
        context.config_gameplay.set_waves(waves_array)

    def definition_current_tile(self, event, context):
        mouse_pose = pygame.mouse.get_pos()  # получает позицию мышки
        context.config_gameplay.set_highlight_tile(None)
        if context.config_parameter_scene.get_width()- context.config_parameter_scene.get_height()* 0.4 > mouse_pose[0] > context.config_parameter_scene.get_height()* 0.4:
            tile_scale = self.__map_array[int(self.__level) - 1].get_tile_scale()
            build_array = self.get_build_array()
            for i in range(len(build_array)):  # Проходит по координатам всех тайлов, и если они совпадут с координатой мышки, то этот тайл сохранится как текущий тайл. Если мышка была нажата, та как действующий тайл
                if build_array[i]['coordinate'][0] <= mouse_pose[0] <= build_array[i]['coordinate'][0] + tile_scale and build_array[i]['coordinate'][1] <= mouse_pose[1] <= \
                        build_array[i]['coordinate'][1] + tile_scale:
                    context.config_gameplay.set_highlight_tile(i)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        context.config_gameplay.set_current_tile(i)
                        context.config_gameplay.set_shop_type(1)
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    context.config_gameplay.set_current_tile(None)
                    context.config_gameplay.set_shop_type(0)

    def get_level(self):
        return int(self.__level) + 1