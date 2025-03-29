import math

import pygame  # импорт библиотеки pygame
import os
from Scripts.MainScripts import Function


class Enemy:
    # инициализация класса
    def __init__(self, image, rect, scale, angle, health, additional_price, position_on_tile, armor = 0, treatment = 0,pos = 0):
        self.__image = pygame.image.load(image)  # картинка
        self.__scale = scale  # размер врага
        self.__image = pygame.transform.scale(self.__image, (self.__scale, self.__scale))
        self.__rect = rect  # массив координаты врага
        self.__pos = pos  # количество кадров, во время которых враг перемещался
        self.__additional_original_price = additional_price  # начальное количество монет, которые дают за врага
        self.__additional_tower_price = 0  # количество монет, которые дают за башню
        self.__armor = armor  # броня
        self.__treatment = treatment  # лечение/яд
        self.__center = [self.__rect[0] + self.__scale / 2, self.__rect[1] + self.__scale / 2]  # центр врага
        self.__health = health  # здоровье
        self.__poison_dict = []
        self.__current_damage_poison = 0
        self.__position_on_tile = position_on_tile
        self.__angle = angle
        self.__animation = []
        self.__x = -1
        files_animation = os.listdir('images/enemy/animationWalking')
        for i in files_animation:
            self.__animation.append(pygame.transform.scale(pygame.image.load('images/enemy/animationWalking/' + i), (self.__scale, self.__scale)))
        self.__rotated_image = self.__image
        self.__current_legs_image = self.__animation[0]
        self.__is_dying = False
        self.__time_dying = 0

    def get_center(self):  # получает центр врага
        self.__center = [self.__rect[0] + self.__scale / 2, self.__rect[1] + self.__scale / 2]
        return self.__center

    def draw(self, context):  # функция, рисующая врага
        self.__rotated_image = pygame.transform.rotate(self.__image, self.__angle)
        if not self.__is_dying:
            if context.get_config_gameplay().get_always_use_additional_parameters() or context.get_config_gameplay().get_use_additional_parameters():
                scale = int(self.__scale * 0.6)
                delta = (abs(math.cos(math.radians(self.__angle))) + abs(math.sin(math.radians(self.__angle)))) * (self.__scale / 2)
                Function.draw_text(str(self.__health), scale, (self.__rect[0] + delta, self.__rect[1] + delta), context)  # Рисует количество хп если используются дополнительный визуал. Не в центре так как размер шрифта не связан с координатами
        else:
            fps = context.get_animation_controller().get_fps()
            if self.__time_dying < fps:
                self.__time_dying += 1
                self.__rotated_image.set_alpha(int(100 * self.__time_dying / fps))
                self.__current_legs_image.set_alpha(int(100 * self.__time_dying / fps))
        context.get_config_parameter_scene().get_screen().blit(self.__rotated_image, self.__rect)
        context.get_config_parameter_scene().get_screen().blit(pygame.transform.rotate(self.__current_legs_image, self.__angle), self.__rect)

    def __set_coordinate_and_angle(self, deltaX, deltaY, t = None):  # получает из координат вектора новое положение врага и угол поворота
        self.__rect[0] += deltaX
        self.__rect[1] += deltaY
        self.__angle = math.atan(deltaX/deltaY) * 180 / math.pi
        if t is not None:
            self.__angle += 180
        self.__pos += 1

    def move(self, time, context, speed = 100):  # движение врага
        tile_scale = context.get_maps_controller().get_tile_scale()
        if self.__pos // speed != len(context.get_maps_controller().get_trajectory()) - 1:
            difference_position = context.get_maps_controller().get_trajectory()[self.__pos // speed + 1] - context.get_maps_controller().get_trajectory()[self.__pos // speed]
        else:
            difference_position = 0
        if difference_position == 0:
            match context.get_maps_controller().get_trajectory()[self.__pos//speed]:  # сравнивает текущую траекторию
                case 0:
                    self.__rect[1] -= (1.2 * tile_scale) / speed
                    self.__pos += 1
                case 1:
                    self.__rect[0] += (1.2 * tile_scale) / speed
                    self.__pos += 1
                case 2:
                    self.__rect[1] += (1.2 * tile_scale) / speed
                    self.__pos += 1
                case 3:
                    self.__rect[0] -= (1.2 * tile_scale) / speed
                    self.__pos += 1
        else:
            x = 6 / speed
            n = self.__pos % speed
            t = None
            if self.__x < 0:
                y = ((n + 1) * x - 1) ** 3 - (n * x - 1) ** 3
                deltaX = x * (1.2 * tile_scale) / 8
            elif self.__x < 2:
                y = ((1 + n) * x - 1)**2 - (n * x - 1)** 2
                deltaX = x * (1.2 * tile_scale) / 8
            else:
                y = - math.sqrt(9 - (n * x - 6) ** 2) + math.sqrt(9 - ((n + 1) * x - 6) ** 2)
                deltaX = (-x) * (1.2 * tile_scale) / 8
                t = 0
            deltaY = y * (1.2 * tile_scale) / 8
            self.__x += x
            if difference_position == 1 or difference_position == -3:
                match context.get_maps_controller().get_trajectory()[self.__pos // speed]:  # сравнивает текущую траекторию
                    case 0:
                        self.__set_coordinate_and_angle(-deltaX, -deltaY, t)
                    case 1:
                        self.__set_coordinate_and_angle(deltaY, -deltaX, t)
                    case 2:
                        self.__set_coordinate_and_angle(deltaX, deltaY, t)
                    case 3:
                        self.__set_coordinate_and_angle(-deltaY, deltaX, t)
            else:
                match context.get_maps_controller().get_trajectory()[self.__pos // speed]:  # сравнивает текущую траекторию
                    case 0:
                        self.__set_coordinate_and_angle(deltaX, -deltaY, t)
                    case 1:
                        self.__set_coordinate_and_angle(deltaY, deltaX, t)
                    case 2:
                        self.__set_coordinate_and_angle(-deltaX, deltaY, t)
                    case 3:
                        self.__set_coordinate_and_angle(-deltaY, -deltaX, t)
        self.__current_legs_image = self.__animation[time % 30]
        if self.__pos // speed == len(context.get_maps_controller().get_trajectory()):
            context.get_config_gameplay().set_is_fail(True)

    def end_walk(self):  # завершает передвижение врага
        self.__x = -1

    def remove_health(self, context): #  убрать хп
        if context.get_towers_controller().get_current_tower().get_armor_piercing():
            self.__health -= context.get_towers_controller().get_current_tower().get_damage()
        else:
            if context.get_towers_controller().get_current_tower().get_damage() - self.__armor > 0:
                self.__health -= context.get_towers_controller().get_current_tower().get_damage() - self.__armor
        if context.get_towers_controller().get_current_tower().get_poison() != 0:
            if self.__current_damage_poison < context.get_towers_controller().get_current_tower().get_poison():
                self.__treatment -= context.get_towers_controller().get_current_tower().get_poison() - self.__current_damage_poison
                self.__current_damage_poison = context.get_towers_controller().get_current_tower().get_poison()
            self.__poison_dict.append({'damage': context.get_towers_controller().get_current_tower().get_poison(), 'time': 2})

    def treat(self):  # отравление/лечение
        if self.__treatment > 0:
            self.__health += self.__treatment
        elif self.__treatment + self.__armor < 0:
            self.__health += self.__treatment + self.__armor
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

    def reset_to_zero_additional_tower_price(self):  # сбрасывает до 0 дополнительное золото от башни
        self.__additional_tower_price = 0

    def new_value_additional_tower_price(self, context):  # обновляет текущую стоимость врага
        self.__additional_tower_price = context.get_towers_controller().get_current_tower().get_additional_money()

    def get_additional_money(self):  # геттер стоимости врага
        return self.__additional_original_price + self.__additional_tower_price

    def get_characteristic(self):  # возвращает словарь из характеристик врага и их значений
        characteristic_dict = {'health': 'health ' + str(self.__health), 'price': 'price ' + str(2 + self.__additional_original_price)}
        if self.__armor != 0:
            characteristic_dict['armor'] = 'armor ' + str(self.__armor)
        if self.__treatment > 0:
            characteristic_dict['healing'] = 'healing ' + str(self.__treatment)
        if self.__treatment < 0:
            characteristic_dict['poison'] = 'venom ' + str(-self.__treatment)
        return characteristic_dict

    def get_scale(self):  # другие геттеры
        return self.__scale

    def get_rect(self):
        return self.__rect

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health += value

    def check_dying(self):
        if self.__health <= 0:
            self.__is_dying = True

    def get_is_dying(self):
        return self.__is_dying

    def get_is_dead(self, fps):
        if self.__time_dying == fps:
            return True
        else:
            return False