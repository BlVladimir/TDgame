from random import randrange
from math import sqrt, atan, pi

import pygame  # импорт библиотеки pygame
import os
from Scripts.MainScripts import Function


class Enemy:
    # инициализация класса
    def __init__(self, image, rect, scale, angle, health, additional_price, position_on_tile, armor = 0, treatment = 0,pos = 0):
        self.__image = pygame.image.load(image)
        self.scale = scale
        self.__image = pygame.transform.scale(self.__image, (self.scale, self.scale))
        self.rect = rect
        self.pos = pos
        self.__additional_original_price = additional_price
        self.__additional_tower_price = 0
        self.__armor = armor
        self.__treatment = treatment
        self.center = [self.rect[0] + self.scale/2, self.rect[1] + self.scale/2]
        self.health = health
        self.test_array = [[rect[0], rect[1]]]
        self.__poison_dict = []
        self.__current_damage_poison = 0
        self.__position_on_tile = position_on_tile
        self.__angle = angle
        self.__animation = []
        self.__x = -1
        files_animation = os.listdir('images/enemy/animationWalking')
        for i in files_animation:
            self.__animation.append(pygame.transform.scale(pygame.image.load('images/enemy/animationWalking/' + i), (self.scale, self.scale)))
        self.__rotated_image = self.__image
        self.__current_legs_image = self.__animation[0]


    def get_center(self):  # получает центр врага
        self.center = [self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2]
        return self.center

    def draw(self, context):  # функция, рисующая врага
        self.__rotated_image = pygame.transform.rotate(self.__image, self.__angle)
        context.get_config_parameter_scene().get_screen().blit(self.__rotated_image, self.rect)
        context.get_config_parameter_scene().get_screen().blit(pygame.transform.rotate(self.__current_legs_image, self.__angle), self.rect)
        if context.get_config_gameplay().get_always_use_additional_parameters() or context.get_config_gameplay().get_use_additional_parameters():
            scale = int(self.scale * 0.6)
            Function.draw_text_from_center(str(self.health), scale, (self.rect[0] + self.scale / 2, self.rect[1] + self.scale / 2), context)  # Рисует количество хп если используются дополнительный визуал. Не в центре так как размер шрифта не связан с координатами

    def __set_coordinate_and_angle(self, deltaX, deltaY):
        self.rect[0] += deltaX
        self.rect[1] += deltaY
        self.__angle = atan(deltaX/deltaY) * 180 / pi
        self.pos += 1

    def move(self, tile_scale, time, context, speed = 100):  # Траектория - это массив поворотов тайла для врагов. Логично, что врагу нужно двигаться в ту сторону, где находится следующий тайл. Промежутки и размер тайлов нужны для определения изменения координат. Скорость - число изменений расстояния в секунду
        if self.pos // speed != len(context.get_maps_controller().get_trajectory()) - 1:
            difference_position = context.get_maps_controller().get_trajectory()[self.pos // speed + 1] - context.get_maps_controller().get_trajectory()[self.pos // speed]
        else:
            difference_position = 0
        if difference_position == 0:
            match context.get_maps_controller().get_trajectory()[self.pos//speed]:  # сравнивает текущую траекторию
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
        else:
            x = 6 / speed
            n = self.pos % speed
            if self.__x < 0:
                y = ((n + 1) * x - 1) ** 3 - (n * x - 1) ** 3
                deltaX = x * (1.2 * tile_scale) / 8
            elif self.__x < 2:
                y = ((1 + n) * x - 1)**2 - (n * x - 1)** 2
                deltaX = x * (1.2 * tile_scale) / 8
            else:
                y = - sqrt(9 - (n * x - 6) ** 2) + sqrt(9 - ((n + 1) * x - 6) ** 2)
                deltaX = (-x) * (1.2 * tile_scale) / 8
            deltaY = y * (1.2 * tile_scale) / 8
            self.__x += x
            if difference_position == 1 or difference_position == -3:
                match context.get_maps_controller().get_trajectory()[self.pos // speed]:  # сравнивает текущую траекторию
                    case 0:
                        self.__set_coordinate_and_angle(-deltaX, -deltaY)
                    case 1:
                        self.__set_coordinate_and_angle(deltaY, -deltaX)
                    case 2:
                        self.__set_coordinate_and_angle(deltaX, deltaY)
                    case 3:
                        self.__set_coordinate_and_angle(-deltaY, deltaX)
            else:
                match context.get_maps_controller().get_trajectory()[self.pos // speed]:  # сравнивает текущую траекторию
                    case 0:
                        self.__set_coordinate_and_angle(deltaX, -deltaY)
                    case 1:
                        self.__set_coordinate_and_angle(deltaY, deltaX)
                    case 2:
                        self.__set_coordinate_and_angle(-deltaX, deltaY)
                    case 3:
                        self.__set_coordinate_and_angle(-deltaY, -deltaX)
        self.__current_legs_image = self.__animation[time % 30]
        if self.pos // speed == len(context.get_maps_controller().get_trajectory()):
            context.get_config_gameplay().set_is_fail(True)

    def end_walk(self):
        self.__x = -1

    def remove_health(self, context): #  убрать хп
        if context.get_towers_controller().get_current_tower().armor_piercing:
            self.health -= context.get_towers_controller().get_current_tower().damage
        else:
            if context.get_towers_controller().get_current_tower().damage - self.__armor > 0:
                self.health -= context.get_towers_controller().get_current_tower().damage - self.__armor
        if context.get_towers_controller().get_current_tower().poison != 0:
            if self.__current_damage_poison < context.get_towers_controller().get_current_tower().poison:
                self.__treatment -= context.get_towers_controller().get_current_tower().poison - self.__current_damage_poison
                self.__current_damage_poison = context.get_towers_controller().get_current_tower().poison
            self.__poison_dict.append({'damage': context.get_towers_controller().get_current_tower().poison, 'time': 2})

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

    def reset_to_zero_additional_tower_price(self):
        self.__additional_tower_price = 0

    def new_value_additional_tower_price(self, context):
        self.__additional_tower_price = context.get_towers_controller().get_current_tower().get_additional_money()

    def get_additional_money(self):
        return self.__additional_original_price + self.__additional_tower_price

    def get_characteristic(self):
        characteristic_array = ['health ' + str(self.health), 'price ' + str(2 + self.__additional_original_price)]
        if self.__armor != 0:
            characteristic_array.append('armor ' + str(self.__armor))
        if self.__treatment > 0:
            characteristic_array.append('healing ' + str(self.__treatment))
        if self.__treatment < 0:
            characteristic_array.append('poisoning ' + str(self.__treatment))
        return characteristic_array


