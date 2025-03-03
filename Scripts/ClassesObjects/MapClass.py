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
        self.tile_array = tile_array  # Двумерный массив, каждый массив которого строчка. Состоит из цифр, каждой из которых соответствует определенный тип тайла
        self.road_array = road_array  # массив кортежей, с координатами дорог
        self.gaps = ceil(0.2 * tile_scale)  # размер промежутков
        self.tile_scale = ceil(tile_scale)   # размер тайлов
        self.__image_tile_mass = [pygame.image.load("images/tile/forEnemies.png"),
                                  pygame.image.load("images/tile/commonBuilding.png"),
                                  pygame.image.load("images/tile/damageUp.png"),  # 2 - урон
                                  pygame.image.load("images/tile/radiusUp.png"),  # 3 - радиус
                                  pygame.image.load("images/tile/antyShield.png"),  # 4 - бронебойный
                                  pygame.image.load("images/tile/poisonUp.png"),  # 5 - ядовитая
                                  pygame.image.load("images/tile/moneyUp.png"),  # 6 - больше денег
                                  pygame.image.load("images/tile/base.png")]  # массив картинок тайлов
        files_animation = listdir('images/tile/destructionBaseAnimation')
        self.__animation_destruction = []
        for i in files_animation:
            self.__animation_destruction.append(pygame.transform.scale(pygame.image.load('images/tile/destructionBaseAnimation/' + i), (tile_scale, tile_scale)))
        self.__image_tile_mass[0] = pygame.transform.scale(self.__image_tile_mass[0], (self.tile_scale, self.tile_scale + self.gaps))  # Меняет размер дороги(так как она прямоугольная)
        for i in range(len(self.__image_tile_mass) - 1):
            self.__image_tile_mass[i + 1] = pygame.transform.scale(self.__image_tile_mass[i + 1], (self.tile_scale, self.tile_scale))  # меняет остальные размеры
        self.coordinates = []  # создает пустой массив координат
        for y in range(len(self.tile_array)):
            for x in range(len(self.tile_array[y])):
                if self.tile_array[y][x] != 0:
                    self.coordinates.append((x, y))  # добавляет в массив координат кортежи координат квадратных тайлов
        for i in range(len(self.coordinates)):
            self.coordinates[i] = get_coordinates(self.coordinates[i], len(tile_array), len(tile_array), 0, 0, width_screen, height_screen, self.gaps, self.tile_scale)
        for i in range(len(self.road_array[1])):
            if self.road_array[1][i] == 0:
                self.road_array[0][i] = get_coordinates(self.road_array[0][i], len(tile_array), len(tile_array), 0, self.gaps, width_screen, height_screen, self.gaps, self.tile_scale)
            elif road_array[1][i] == 3:
                self.road_array[0][i] = get_coordinates(self.road_array[0][i], len(tile_array), len(tile_array), self.gaps, 0, width_screen, height_screen, self.gaps, self.tile_scale)
            else:
                self.road_array[0][i] = get_coordinates(self.road_array[0][i], len(tile_array), len(tile_array), 0, 0, width_screen,
                                                        height_screen, self.gaps, self.tile_scale)  # заменяет кортежи номера дорог на кортежи с координатами дорог
        self.build_array = []
        number = 0
        for i in range(len(self.tile_array)):
            for j in self.tile_array[i]:
                if j != 0:
                    if j != 8:
                        self.build_array.append({'coordinate': self.coordinates[number], 'type': j, 'is_filled': False})
                    number += 1

    def get_trajectory_array(self):
        return self.road_array[1]

    def draw(self, context):
        p = 0
        for y in range(len(self.tile_array)):
            for x in range(len(self.tile_array[y])):
                if self.tile_array[y][x] != 0 and self.tile_array[y][x] != 8:
                    context.get_config_parameter_scene().get_screen().blit(self.__image_tile_mass[self.tile_array[y][x]], self.coordinates[p])
                    p += 1
                elif self.tile_array[y][x] == 8 and not context.get_config_gameplay().get_is_fail():
                    context.get_config_parameter_scene().get_screen().blit(self.__image_tile_mass[1], self.coordinates[p])
                    context.get_config_parameter_scene().get_screen().blit(self.__image_tile_mass[7], self.coordinates[p])
                    p += 1
                elif self.tile_array[y][x] == 8 and context.get_config_gameplay().get_is_fail():
                    time = context.get_animation_controller().get_time_game_over()
                    if time < 30:
                        context.get_config_parameter_scene().get_screen().blit(self.__image_tile_mass[1], self.coordinates[p])
                        context.get_config_parameter_scene().get_screen().blit(self.__animation_destruction[time // 2], self.coordinates[p])
                    else:
                        context.get_config_parameter_scene().get_screen().blit(self.__image_tile_mass[1], self.coordinates[p])
                        context.get_config_parameter_scene().get_screen().blit(self.__animation_destruction[14], self.coordinates[p])
                    p += 1
        for i in range(len(self.road_array[0])):
            context.get_config_parameter_scene().get_screen().blit(pygame.transform.rotate(self.__image_tile_mass[0], self.road_array[1][i] * (-90)), self.road_array[0][i])   # Функция рисует тайлы. Дороги отдельно от остальных

    def get_started_position(self, position_enemy_on_tile):
        rectEnemy = [0, 0]
        if self.road_array[1][0] == 0:
            rectEnemy[0], rectEnemy[1] = self.road_array[0][0][0], self.road_array[0][0][1] + self.gaps
        elif self.road_array[1][0] == 3:
            rectEnemy[0], rectEnemy[1] = self.road_array[0][0][0] + self.gaps, self.road_array[0][0][1]
        else:
            rectEnemy[0], rectEnemy[1] = self.road_array[0][0][0], self.road_array[0][0][1]
        rectEnemy[0], rectEnemy[1] = rectEnemy[0] + self.tile_scale / 4, rectEnemy[1] + self.tile_scale / 4
        if position_enemy_on_tile == 1:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] - self.tile_scale / 4, rectEnemy[1] - self.tile_scale / 4
        elif position_enemy_on_tile == 2:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] + self.tile_scale / 4, rectEnemy[1] + self.tile_scale / 4
        elif position_enemy_on_tile == 3:
            rectEnemy[1] = rectEnemy[1] - self.tile_scale / 4
        elif position_enemy_on_tile == 4:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] - self.tile_scale / 4, rectEnemy[1] + self.tile_scale / 4
        return rectEnemy

    def get_started_angel(self):
        return (-90) * self.road_array[1][0]

    def get_tile_scale(self):
        return self.tile_scale



