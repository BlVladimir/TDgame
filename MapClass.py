import pygame  # импорт библиотеки pygame


def getCoordinates(coordinates, tileValueX, tileValueY, xBais, yBais, widthScreen, heightScreen, gaps, tileScale):
    coordinates = (
            widthScreen / 2 - (tileValueX / 2) * (tileScale + gaps) + coordinates[0] * (
                    tileScale + gaps) - xBais,
            heightScreen / 2 - (tileValueY / 2) * (tileScale + gaps) + coordinates[1] * (
                    tileScale + gaps) - yBais)
    return coordinates  # метод делает из кортежа с номером по вертикали и горизонтали тайла координаты этого тайла, с помощью количества тайлов по вертикали и горизонтали, промежутков, смещения(для прямоугольников), размеров экрана(чтобы было по центру), промежутков между тайлами и размерами тайла


class Map:
    # инициализация класса
    def __init__(self, tileMas, roadMas, widthScreen, heightScreen, gaps, tileScale):
        self.tileMas = tileMas  # двумерный массив, каждый массив которого строчка. Состоит из цифр, каждой из которых соответствует определенный тип тайла
        self.roadMas = roadMas  # массив кортежей, с координатами дорог
        self.gaps = gaps  # размер промежутков
        self.tileScale = tileScale  # размер тайлов
        self.imageTileMass = [pygame.image.load("images/tile/forEnemies.png"),
                              pygame.image.load("images/tile/commonBuilding.png"),
                              pygame.image.load("images/tile/damageUp.png"),
                              pygame.image.load("images/tile/radiusUp.png"),
                              pygame.image.load("images/tile/antyShield.png"),
                              pygame.image.load("images/tile/poisonUp.png"),
                              pygame.image.load("images/tile/antyInvisibility.png"),
                              pygame.image.load("images/tile/moneyUp.png")]  # массив картинок тайлов
        self.imageTileMass[0] = pygame.transform.scale(self.imageTileMass[0], (self.tileScale, self.tileScale + self.gaps))  # меняет размер дороги(т.к. она прямоугольная)
        for i in range(len(self.imageTileMass) - 1):
            self.imageTileMass[i + 1] = pygame.transform.scale(self.imageTileMass[i + 1], (self.tileScale, self.tileScale))  # меняет остальные размеры
        self.coordinates = []  # создает пустой массив координат
        for y in range(len(self.tileMas)):
            for x in range(len(self.tileMas[y])):
                if self.tileMas[y][x] != 0:
                    self.coordinates.append((x, y))  # добавляет в массив координат кортежи координат квадратных тайлов
        for i in range(len(self.coordinates)):
            self.coordinates[i] = getCoordinates(self.coordinates[i], len(tileMas), len(tileMas), 0, 0, widthScreen, heightScreen, self.gaps, self.tileScale)
        for i in range(len(roadMas[1])):
            if roadMas[1][i] == 0:
                roadMas[0][i] = getCoordinates(roadMas[0][i], len(tileMas), len(tileMas), 0, self.gaps, widthScreen, heightScreen, self.gaps, self.tileScale)
            elif roadMas[1][i] == 1:
                roadMas[0][i] = getCoordinates(roadMas[0][i], len(tileMas), len(tileMas), self.gaps, 0, widthScreen, heightScreen, self.gaps, self.tileScale)
            else:
                roadMas[0][i] = getCoordinates(roadMas[0][i], len(tileMas), len(tileMas), 0, 0, widthScreen,
                                               heightScreen, self.gaps, self.tileScale)  # заменяет кортежи номера дорог на кортежи с координатами дорог
        self.buildMass = []
        for i in range(len(self.tileMas)):
            for j in range(len(self.tileMas[i])):
                if tileMas[i][j] != 0:
                    self.buildMass.append([0,0])

    def getTrajectory(self, trajectory):
        trajectory = self.roadMas[1]
        return trajectory

    def draw(self, screen):
        p = 0
        for y in range(len(self.tileMas)):
            for x in range(len(self.tileMas[y])):
                if self.tileMas[y][x] != 0:
                    screen.blit(self.imageTileMass[self.tileMas[y][x]], self.coordinates[p])
                    p += 1
        for i in range(len(self.roadMas[0])):
            screen.blit(pygame.transform.rotate(self.imageTileMass[0], self.roadMas[1][i] * 90), self.roadMas[0][i])   # функция рисует тайлы. Дороги отдельно от остальных
