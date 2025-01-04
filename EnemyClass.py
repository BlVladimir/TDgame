from random import randrange

import pygame  # импорт библиотеки pygame
import Map
import Function


class Enemy:
    # инициализация класса
    def __init__(self, image, rect, scale, health, pos = 0):
        self.image = pygame.image.load(image)
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = rect
        self.pos = pos
        self.center = [self.rect[0] + self.scale/2, self.rect[1] + self.scale/2]
        self.health =health

    def get_center(self):
        self.center = [self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2]
        return self.center

    def draw(self, screen, always_use, use_additional_parameters):  # функция, рисующая врага
        screen.blit(self.image, self.rect)
        if always_use or use_additional_parameters:
            scale = int(self.scale * 0.6)
            Function.draw_text(screen, str(self.health), scale, (self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2))  # Рисует количество хп если используются дополнительный визуал. Не в центре так как размер шрифта не связан с координатами

    def move(self, trajectory, gaps, tile_scale, speed = 100):  # Траектория - это массив поворотов тайла для врагов. Логично, что врагу нужно двигаться в ту сторону, где находится следующий тайл. Промежутки и размер тайлов нужны для определения изменения координат. Скорость - число изменений расстояния в секунду
        if self.pos//speed != len(trajectory):  # Проверяет, что существует следующая позиция
            match trajectory[self.pos//speed]:  # сравнивает текущую траекторию
                case 0:
                    self.rect[1] -= (gaps + tile_scale) / speed
                    self.pos += 1
                case 1:
                    self.rect[0] += (gaps + tile_scale) / speed
                    self.pos += 1
                case 2:
                    self.rect[1] += (gaps + tile_scale) / speed
                    self.pos += 1
                case 3:
                    self.rect[0] -= (gaps + tile_scale) / speed
                    self.pos += 1
            return False
        else:
            return True

    def remove_health(self, damage): #  убрать хп
        self.health -= damage


def create_waves(number_of_waves, lvl):  # Функция создает массив заданной длины, состоящий из 1, 2 и 3. Нужен для определения количества врагов на каждой волне
    waves_mas = [[]]
    for i in range(number_of_waves):
        waves_mas[i].append(randrange(1, 4))
        waves_mas[i].append(randrange(0, lvl + 1))
        if i != number_of_waves - 1:
            waves_mas.append([])
    waves_mas[0][1] = 0
    return waves_mas


def create_enemy_on_lvl1(waves_mas, current_wave, enemy_mas):  # Добавляет в массив врагов новые элементы. В зависимости от количества врагов у каждого врага разные координаты
    image_enemy = 'images/enemy/common.png'
    health = 3
    match waves_mas[current_wave][1]:
        case 1:
            image_enemy = 'images/enemy/armoredEnemy.png'
            health = 6
    if waves_mas[current_wave][0] == 1:
        enemy_mas.append(Enemy(image_enemy, Map.lvl1.get_started_position(0), Map.lvl1.tile_scale / 2, health))
    elif waves_mas[current_wave][0] == 2:
        enemy_mas.append(Enemy(image_enemy, Map.lvl1.get_started_position(1), Map.lvl1.tile_scale / 2, health))
        enemy_mas.append(Enemy(image_enemy, Map.lvl1.get_started_position(2), Map.lvl1.tile_scale / 2, health))
    elif waves_mas[current_wave][0] == 3:
        enemy_mas.append(Enemy(image_enemy, Map.lvl1.get_started_position(3), Map.lvl1.tile_scale / 2, health))
        enemy_mas.append(Enemy(image_enemy, Map.lvl1.get_started_position(4), Map.lvl1.tile_scale / 2, health))
        enemy_mas.append(Enemy(image_enemy, Map.lvl1.get_started_position(2), Map.lvl1.tile_scale / 2, health))

def move_all_enemies(enemy_mas, trajectory, gaps, tile_scale, speed = 60):  # двигает всех врагов
    isFail = False
    for i in range(len(enemy_mas)):
        isFail = enemy_mas[i].move(trajectory, gaps, tile_scale, speed)
        if isFail:
            break
    return isFail