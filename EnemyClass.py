from random import randrange

import pygame  # импорт библиотеки pygame
import os
import Function


class Enemy:
    # инициализация класса
    def __init__(self, image, rect, scale, health, armor =0, treatment = 0,pos = 0):
        self.__image = pygame.image.load(image)
        self.scale = scale
        self.__image = pygame.transform.scale(self.__image, (self.scale, self.scale))
        self.rect = rect
        self.pos = pos
        self.__armor = armor
        self.__treatment = treatment
        self.center = [self.rect[0] + self.scale/2, self.rect[1] + self.scale/2]
        self.health = health
        self.__poison_dict = []
        self.__current_damage_poison = 0
        self.__angle = 0
        self.__animation = []
        files_animation = os.listdir('images/enemy/animationWalking')
        for i in files_animation:
            self.__animation.append(pygame.transform.scale(pygame.image.load('images/enemy/animationWalking/' + i), (self.scale, self.scale)))
        self.__rotated_image = self.__image
        self.__legs_image = self.__animation[0]


    def get_center(self):  # получает центр врага
        self.center = [self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2]
        return self.center

    def draw(self, context):  # функция, рисующая врага
        context.get_config_parameter_scene().get_screen().blit(self.__rotated_image, self.rect)
        context.get_config_parameter_scene().get_screen().blit(self.__legs_image, self.rect)
        if context.get_config_gameplay().get_always_use_additional_parameters() or context.get_config_gameplay().get_use_additional_parameters():
            scale = int(self.scale * 0.6)
            Function.draw_text(str(self.health), scale, (self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2), context)  # Рисует количество хп если используются дополнительный визуал. Не в центре так как размер шрифта не связан с координатами

    def move(self, tile_scale, time, maps_controller, context, speed = 100):  # Траектория - это массив поворотов тайла для врагов. Логично, что врагу нужно двигаться в ту сторону, где находится следующий тайл. Промежутки и размер тайлов нужны для определения изменения координат. Скорость - число изменений расстояния в секунду
        if self.pos // speed != len(maps_controller.get_trajectory()) - 1:
            difference_position = maps_controller.get_trajectory()[self.pos // speed + 1] - maps_controller.get_trajectory()[self.pos // speed]
        else:
            difference_position = 0
        match maps_controller.get_trajectory()[self.pos//speed]:  # сравнивает текущую траекторию
            case 0:
                self.rect[1] -= (1.2 * tile_scale) / speed
                self.pos += 1
            case 1:
                self.rect[0] += (1.2 * tile_scale) / speed
                self.pos += 1
            case 2:
                self.rect[1] += (1.2 * tile_scale) / speed
                self.pos += 1
            case 3:
                self.rect[0] -= (1.2 * tile_scale) / speed
                self.pos += 1
        if difference_position > 0:
            self.__angle -= 90 / speed
        elif difference_position < 0:
            self.__angle += 90 / speed
        self.__legs_image = pygame.transform.rotate(self.__animation[time % 30], self.__angle)
        self.__rotated_image = pygame.transform.rotate(self.__image, self.__angle)
        if self.pos // speed == len(maps_controller.get_trajectory()):
            context.get_config_gameplay().new_value_is_fail(True)

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


def create_waves(number_of_waves, lvl, context):  # Функция создает массив заданной длины, состоящий из 1, 2 и 3. Нужен для определения количества врагов на каждой волне
    waves_array = [[]]
    for i in range(number_of_waves):
        waves_array[i].append(randrange(1, 4))
        waves_array[i].append(randrange(0, lvl + 1))
        if i != number_of_waves - 1:
            waves_array.append([])
    waves_array[0][1] = 0
    context.get_config_gameplay().new_value_waves(waves_array)

