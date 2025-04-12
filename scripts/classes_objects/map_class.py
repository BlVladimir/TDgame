import pygame  # импорт библиотеки pygame

from os import listdir
from math import ceil

def get_coordinates(coordinates, tileValueX, tileValueY, xBais, yBais, widthScreen, heightScreen, gaps, tileScale):
    coordinates = (
            widthScreen / 2 - (tileValueX / 2) * (tileScale + gaps) + coordinates[0] * (
                    tileScale + gaps) - xBais,
            heightScreen / 2 - (tileValueY / 2) * (tileScale + gaps) + coordinates[1] * (
                    tileScale + gaps) - yBais)
    return coordinates  # метод делает из кортежа с номером по вертикали и горизонтали тайла координаты этого тайла, с помощью количества тайлов по вертикали и горизонтали, промежутков, смещения(для прямоугольников), размеров экрана(чтобы было по центру), промежутков между тайлами и размерами тайла


class Map:
    # инициализация класса
    def __init__(self, tile_array, road_array, width_screen, height_screen, tile_scale):
        self.__tile_array = tile_array  # Двумерный массив, каждый массив которого строчка. Состоит из цифр, каждой из которых соответствует определенный тип тайла
        self.__road_array = road_array  # массив кортежей, с координатами дорог
        self.__gaps = ceil(0.2 * tile_scale)  # размер промежутков
        self.__tile_scale = ceil(tile_scale)   # размер тайлов
        self.__image_tile_mass = [pygame.image.load("images/tile/for_enemies.png"),
                                  pygame.image.load("images/tile/common_building.png"),
                                  pygame.image.load("images/tile/damage_up.png"),  # 2 - урон
                                  pygame.image.load("images/tile/radius_up.png"),  # 3 - радиус
                                  pygame.image.load("images/tile/anty_shield.png"),  # 4 - бронебойный
                                  pygame.image.load("images/tile/poison_up.png"),  # 5 - ядовитая
                                  pygame.image.load("images/tile/money_up.png"),  # 6 - больше денег
                                  pygame.image.load("images/tile/base.png")]  # массив картинок тайлов
        files_animation = listdir('images/tile/destruction_base_animation')
        self.__animation_destruction = []
        for i in files_animation:
            self.__animation_destruction.append(pygame.transform.scale(pygame.image.load('images/tile/destruction_base_animation/' + i), (tile_scale, tile_scale)))
        self.__image_tile_mass[0] = pygame.transform.scale(self.__image_tile_mass[0], (self.__tile_scale, self.__tile_scale + self.__gaps))  # Меняет размер дороги(так как она прямоугольная)
        for i in range(len(self.__image_tile_mass) - 1):
            self.__image_tile_mass[i + 1] = pygame.transform.scale(self.__image_tile_mass[i + 1], (self.__tile_scale, self.__tile_scale))  # меняет остальные размеры
        self.__coordinates = []  # создает пустой массив координат
        for y in range(len(self.__tile_array)):
            for x in range(len(self.__tile_array[y])):
                if self.__tile_array[y][x] != 0:
                    self.__coordinates.append((x, y))  # добавляет в массив координат кортежи координат квадратных тайлов
        for i in range(len(self.__coordinates)):
            self.__coordinates[i] = get_coordinates(self.__coordinates[i], len(tile_array), len(tile_array), 0, 0, width_screen, height_screen, self.__gaps, self.__tile_scale)
        for i in range(len(self.__road_array[1])):
            if self.__road_array[1][i] == 0:
                self.__road_array[0][i] = get_coordinates(self.__road_array[0][i], len(tile_array), len(tile_array), 0, self.__gaps, width_screen, height_screen, self.__gaps, self.__tile_scale)
            elif road_array[1][i] == 3:
                self.__road_array[0][i] = get_coordinates(self.__road_array[0][i], len(tile_array), len(tile_array), self.__gaps, 0, width_screen, height_screen, self.__gaps, self.__tile_scale)
            else:
                self.__road_array[0][i] = get_coordinates(self.__road_array[0][i], len(tile_array), len(tile_array), 0, 0, width_screen,
                                                          height_screen, self.__gaps, self.__tile_scale)  # заменяет кортежи номера дорог на кортежи с координатами дорог
        self.__build_array = []
        number = 0
        for i in range(len(self.__tile_array)):
            for j in self.__tile_array[i]:
                if j != 0:
                    if j != 8:
                        self.__build_array.append({'coordinate': self.__coordinates[number], 'type': j, 'is_filled': False})
                    number += 1

    def get_trajectory_array(self):  # возвращает массив траектории врага
        return self.__road_array[1]

    def draw(self, context):  # рисует карту
        p = 0
        for y in range(len(self.__tile_array)):
            for x in range(len(self.__tile_array[y])):
                if self.__tile_array[y][x] != 0 and self.__tile_array[y][x] != 8:
                    context.config_parameter_scene.get_screen().blit(self.__image_tile_mass[self.__tile_array[y][x]], self.__coordinates[p])
                    p += 1
                elif self.__tile_array[y][x] == 8 and not context.config_gameplay.get_is_fail():
                    context.config_parameter_scene.get_screen().blit(self.__image_tile_mass[1], self.__coordinates[p])
                    context.config_parameter_scene.get_screen().blit(self.__image_tile_mass[7], self.__coordinates[p])
                    p += 1
                elif self.__tile_array[y][x] == 8 and context.config_gameplay.get_is_fail():
                    time = context.animation_controller.get_time_game_over()
                    if time < 30:
                        context.config_parameter_scene.get_screen().blit(self.__image_tile_mass[1], self.__coordinates[p])
                        context.config_parameter_scene.get_screen().blit(self.__animation_destruction[time // 2], self.__coordinates[p])
                    else:
                        context.config_parameter_scene.get_screen().blit(self.__image_tile_mass[1], self.__coordinates[p])
                        context.config_parameter_scene.get_screen().blit(self.__animation_destruction[14], self.__coordinates[p])
                    p += 1
        for i in range(len(self.__road_array[0])):
            context.config_parameter_scene.get_screen().blit(pygame.transform.rotate(self.__image_tile_mass[0], self.__road_array[1][i] * (-90)), self.__road_array[0][i])   # Функция рисует тайлы. Дороги отдельно от остальных

    def get_started_position(self, position_enemy_on_tile):  # возвращает массив координат начального положения врага
        rectEnemy = [0, 0]
        if self.__road_array[1][0] == 0:
            rectEnemy[0], rectEnemy[1] = self.__road_array[0][0][0], self.__road_array[0][0][1] + self.__gaps
        elif self.__road_array[1][0] == 3:
            rectEnemy[0], rectEnemy[1] = self.__road_array[0][0][0] + self.__gaps, self.__road_array[0][0][1]
        else:
            rectEnemy[0], rectEnemy[1] = self.__road_array[0][0][0], self.__road_array[0][0][1]
        rectEnemy[0], rectEnemy[1] = rectEnemy[0] + self.__tile_scale / 4, rectEnemy[1] + self.__tile_scale / 4
        if position_enemy_on_tile == 1:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] - self.__tile_scale / 4, rectEnemy[1] - self.__tile_scale / 4
        elif position_enemy_on_tile == 2:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] + self.__tile_scale / 4, rectEnemy[1] + self.__tile_scale / 4
        elif position_enemy_on_tile == 3:
            rectEnemy[1] = rectEnemy[1] - self.__tile_scale / 4
        elif position_enemy_on_tile == 4:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] - self.__tile_scale / 4, rectEnemy[1] + self.__tile_scale / 4
        return rectEnemy

    def get_started_angel(self):  # возвращает начальный угол поворота для врага
        return (-90) * self.__road_array[1][0]

    def get_tile_scale(self):  # другие геттеры
        return self.__tile_scale

    def get_build_array(self):
        return self.__build_array