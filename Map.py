import pygame  # импорт библиотеки pygame
import MainManu


def get_coordinates(coordinates, tileValueX, tileValueY, xBais, yBais, widthScreen, heightScreen, gaps, tileScale):
    coordinates = (
            widthScreen / 2 - (tileValueX / 2) * (tileScale + gaps) + coordinates[0] * (
                    tileScale + gaps) - xBais,
            heightScreen / 2 - (tileValueY / 2) * (tileScale + gaps) + coordinates[1] * (
                    tileScale + gaps) - yBais)
    return coordinates  # метод делает из кортежа с номером по вертикали и горизонтали тайла координаты этого тайла, с помощью количества тайлов по вертикали и горизонтали, промежутков, смещения(для прямоугольников), размеров экрана(чтобы было по центру), промежутков между тайлами и размерами тайла


class Map:
    # инициализация класса
    def __init__(self, tile_array, road_array, width_screen, height_screen, gaps, tile_scale):
        self.tile_array = tile_array  # Двумерный массив, каждый массив которого строчка. Состоит из цифр, каждой из которых соответствует определенный тип тайла
        self.road_array = road_array  # массив кортежей, с координатами дорог
        self.gaps = gaps  # размер промежутков
        self.tile_scale = tile_scale  # размер тайлов
        self.__image_tile_mass = [pygame.image.load("images/tile/forEnemies.png"),
                                  pygame.image.load("images/tile/commonBuilding.png"),
                                  pygame.image.load("images/tile/damageUp.png"),  # 2 - урон
                                  pygame.image.load("images/tile/radiusUp.png"),  # 3 - радиус
                                  pygame.image.load("images/tile/antyShield.png"),
                                  pygame.image.load("images/tile/poisonUp.png"),
                                  pygame.image.load("images/tile/antyInvisibility.png"),
                                  pygame.image.load("images/tile/moneyUp.png")]  # массив картинок тайлов
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
            elif road_array[1][i] == 1:
                self.road_array[0][i] = get_coordinates(self.road_array[0][i], len(tile_array), len(tile_array), self.gaps, 0, width_screen, height_screen, self.gaps, self.tile_scale)
            else:
                self.road_array[0][i] = get_coordinates(self.road_array[0][i], len(tile_array), len(tile_array), 0, 0, width_screen,
                                                        height_screen, self.gaps, self.tile_scale)  # заменяет кортежи номера дорог на кортежи с координатами дорог
        self.build_array = []
        number = 0
        for i in range(len(self.tile_array)):
            for j in self.tile_array[i]:
                if j != 0:
                    self.build_array.append({'coordinate': self.coordinates[number], 'type': j, 'is_filled': False})
                    number += 1

    def get_trajectory(self):
        trajectory = self.road_array[1]
        return trajectory

    def draw(self, screen):
        p = 0
        for y in range(len(self.tile_array)):
            for x in range(len(self.tile_array[y])):
                if self.tile_array[y][x] != 0:
                    screen.blit(self.__image_tile_mass[self.tile_array[y][x]], self.coordinates[p])
                    p += 1
        for i in range(len(self.road_array[0])):
            screen.blit(pygame.transform.rotate(self.__image_tile_mass[0], self.road_array[1][i] * 90), self.road_array[0][i])   # Функция рисует тайлы. Дороги отдельно от остальных

    def get_started_position(self, tipeOnTile):
        rectEnemy = [0, 0]
        if self.road_array[1][len(self.road_array[1]) - 1] == 0:
            rectEnemy[0], rectEnemy[1] = self.road_array[0][len(self.road_array[0]) - 1][0], self.road_array[0][len(self.road_array[0]) - 1][1] + self.gaps
        elif self.road_array[1][len(self.road_array[1]) - 1] == 1:
            rectEnemy[0], rectEnemy[1] = self.road_array[0][len(self.road_array[0]) - 1][0] + self.gaps, self.road_array[0][len(self.road_array[0]) - 1][1]
        else:
            rectEnemy[0], rectEnemy[1] = self.road_array[0][len(self.road_array[0]) - 1][0], self.road_array[0][len(self.road_array[0]) - 1][1]
        rectEnemy[0], rectEnemy[1] = rectEnemy[0] + self.tile_scale / 4, rectEnemy[1] + self.tile_scale / 4
        if tipeOnTile == 1:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] - self.tile_scale / 4, rectEnemy[1] - self.tile_scale / 4
        elif tipeOnTile == 2:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] + self.tile_scale / 4, rectEnemy[1] + self.tile_scale / 4
        elif tipeOnTile == 3:
            rectEnemy[1] = rectEnemy[1] - self.tile_scale / 4
        elif tipeOnTile == 4:
            rectEnemy[0], rectEnemy[1] = rectEnemy[0] - self.tile_scale / 4, rectEnemy[1] + self.tile_scale / 4
        return rectEnemy

    # def getTipeOfTile(self):





lvl1 = Map([[0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [2, 0, 3, 0, 3],
            [0, 0, 0, 0, 2],
            [1, 0, 1, 0, 1]],
           [[(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 4)], [0, 1, 1, 0, 0, 3, 3, 0]], MainManu.width, MainManu.height,
           20, 100)
lvl2 = Map([[1, 0, 0, 0, 1],
            [1, 2, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 4, 0],
            [0, 1, 3, 0, 0]],
           [[(0, 4), (0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0)],
            [0, 0, 3, 3, 3, 0, 0, 1, 1, 1]], MainManu.width, MainManu.height,
           20, 100)
lvl3 = Map([[0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 4, 0, 0, 1],
            [0, 5, 2, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 3, 0],
            [1, 0, 0, 0, 1, 0, 0]],
           [[(0, 3), (5, 1), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (1, 3)], [3, 0, 3, 0, 3, 0, 0, 3, 3, 2]], MainManu.width, MainManu.height,
           20, 100)
lvl4 = Map([[0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 3, 0],
            [1, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1],
            [5, 0, 4, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 2, 0, 0, 0]],
           [[(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (3, 2)], [2, 1, 2, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 2]], MainManu.width, MainManu.height,
           20, 100)
lvl5 = Map([[0, 0, 0, 0, 1, 0, 0],
            [1, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 5],
            [1, 0, 1, 7, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 3, 4, 0, 0],
            [0, 0, 0, 0, 0, 1, 0]],
           [[(6, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4)], [1, 0, 0, 0, 0 , 1, 1, 2, 1, 1, 2, 2, 2]], MainManu.width, MainManu.height,
           20, 100)
lvl6 = Map([[0, 0, 1, 0, 0, 6, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 3, 0, 4, 0, 1],
            [0, 1, 0, 5, 0, 0, 2],
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 7, 0, 0]],
           [[(2, 6), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)], [0, 3, 3, 3, 0, 0, 0, 0, 1, 1, 1, 1, 2]], MainManu.width, MainManu.height,
           20, 100)  # объекты карт
