from random import randrange

import pygame  # импорт библиотеки pygame
import Map
import Function


class Enemy:
    # инициализация класса
    def __init__(self, image, rect, scale, health, armor =0, treatment = 0,pos = 0):
        self.image = pygame.image.load(image)
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = rect
        self.pos = pos
        self.__armor = armor
        self.__treatment = treatment
        self.center = [self.rect[0] + self.scale/2, self.rect[1] + self.scale/2]
        self.health = health
        self.__poison_dict = []
        self.__current_damage_poison = 0

    def get_center(self):  # получает центр врага
        self.center = [self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2]
        return self.center

    def draw(self, always_use, use_additional_parameters, context):  # функция, рисующая врага
        context.get_config_parameter_scene().get_screen().blit(self.image, self.rect)
        if always_use or use_additional_parameters:
            scale = int(self.scale * 0.6)
            Function.draw_text(str(self.health), scale, (self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2), context)  # Рисует количество хп если используются дополнительный визуал. Не в центре так как размер шрифта не связан с координатами

    def move(self, gaps, tile_scale, context, speed = 100):  # Траектория - это массив поворотов тайла для врагов. Логично, что врагу нужно двигаться в ту сторону, где находится следующий тайл. Промежутки и размер тайлов нужны для определения изменения координат. Скорость - число изменений расстояния в секунду
        if self.pos//speed != len(context.get_config_enemy().get_trajectory()):  # Проверяет, что существует следующая позиция
            match context.get_config_enemy().get_trajectory()[self.pos//speed]:  # сравнивает текущую траекторию
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

    def remove_health(self, damage, armor_piercing, poison): #  убрать хп
        if armor_piercing:
            self.health -= damage
        else:
            if damage - self.__armor > 0:
                self.health -= damage - self.__armor
        if poison != 0:
            if self.__current_damage_poison < poison:
                self.__treatment -= poison - self.__current_damage_poison
                self.__current_damage_poison = poison
            self.__poison_dict.append({'damage': poison, 'time': 2})

    def treat(self):  # отравление/лечение
        if self.__treatment > 0:
            self.health += self.__treatment
        elif self.__treatment + self.__armor < 0:
            self.health += self.__treatment + self.__armor
        remove_array = []
        for i in range(len(self.__poison_dict)):
            self.__poison_dict[i]['time'] -= 1
            if self.__poison_dict[i]['time'] == 0:
                remove_array.append(i)
        if remove_array:
            for i in range(len(remove_array)):
                self.__poison_dict.pop(remove_array[i])
            max_damage = 0
            for i in range(len(self.__poison_dict)):
                if self.__poison_dict[i]['damage'] > max_damage:
                    max_damage = self.__poison_dict[i]['damage']
            self.__treatment -= max_damage - self.__current_damage_poison
            self.__current_damage_poison = max_damage


def create_waves(number_of_waves, lvl):  # Функция создает массив заданной длины, состоящий из 1, 2 и 3. Нужен для определения количества врагов на каждой волне
    waves_mas = [[]]
    for i in range(number_of_waves):
        waves_mas[i].append(randrange(1, 4))
        waves_mas[i].append(randrange(0, lvl + 1))
        if i != number_of_waves - 1:
            waves_mas.append([])
    waves_mas[0][1] = 0
    return waves_mas


def create_enemy_on_lvl1(waves_mas, current_wave, context):  # Добавляет в массив врагов новые элементы. В зависимости от количества врагов у каждого врага разные координаты
    if (current_wave + 1) % 4 == 0:
        additional_health = ((current_wave + 1) // 4 - 1) * 2 + 1
    else:
        additional_health = ((current_wave + 1) // 4) * 2 + (current_wave + 1) % 4 - 1
    additional_health += randrange(-1, 2)
    image_enemy = 'images/enemy/common.png'
    health = 3
    armor = 0
    treatment = 0
    match waves_mas[current_wave][1]:
        case 1:
            image_enemy = 'images/enemy/armoredEnemy.png'
            health = 6
        case 2:
            image_enemy = 'images/enemy/ShieldEnemy.png'
            armor = 3
        case 3:
            image_enemy = 'images/enemy/regen.png'
            health = 4
            treatment = 2
    level1 = context.get_config_map().get_map_array()[0]
    enemy_array = context.get_config_enemy().get_enemy_array()
    if waves_mas[current_wave][0] == 1:
        enemy_array.append(Enemy(image_enemy, level1.get_started_position(0), level1.tile_scale / 2, health + additional_health, armor=armor, treatment=treatment))
        context.get_config_enemy().new_value_enemy_array(enemy_array)
    elif waves_mas[current_wave][0] == 2:
        enemy_array.append(Enemy(image_enemy, level1.get_started_position(1), level1.tile_scale / 2, health + additional_health, armor=armor, treatment=treatment))
        enemy_array.append(Enemy(image_enemy, level1.get_started_position(2), level1.tile_scale / 2, health + additional_health, armor=armor, treatment=treatment))
        context.get_config_enemy().new_value_enemy_array(enemy_array)
    elif waves_mas[current_wave][0] == 3:
        enemy_array.append(Enemy(image_enemy, level1.get_started_position(2), level1.tile_scale / 2, health + additional_health, armor=armor, treatment=treatment))
        enemy_array.append(Enemy(image_enemy, level1.get_started_position(3), level1.tile_scale / 2, health + additional_health, armor=armor, treatment=treatment))
        enemy_array.append(Enemy(image_enemy, level1.get_started_position(4), level1.tile_scale / 2, health + additional_health, armor=armor, treatment=treatment))
        context.get_config_enemy().new_value_enemy_array(enemy_array)

def move_all_enemies(gaps, tile_scale, context, speed = 60):  # двигает всех врагов
    is_fail = False
    enemy_array = context.get_config_enemy().get_enemy_array()
    for i in range(len(enemy_array)):
        is_fail = enemy_array[i].move(gaps, tile_scale, speed, context)
        if is_fail:
            break
    context.get_config_enemy().new_value_enemy_array(enemy_array)
    return is_fail