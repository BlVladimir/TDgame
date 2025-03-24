import pygame  # импорт библиотеки pygame
import math


class Tower:
    # инициализация класса
    def __init__(self, image_foundation, scale, damage, coordinate, index, improve_cost_array, armor_piercing, poison, additional_money = 0, image_gun = None, radius = None):
        self.__is_used = False
        self.__index = index
        self.__image_foundation = pygame.image.load(image_foundation)
        self.__image_foundation = pygame.transform.scale(self.__image_foundation, (scale, scale))
        self.__damage = damage
        self.__scale = scale
        self.__coordinate = coordinate
        self.__angle = 0
        self.__armor_piercing = armor_piercing
        self.__poison = poison
        self.__level = 1
        self.__improve_cost_array = improve_cost_array
        self.__additional_money = additional_money
        if image_gun is not None:
            self.__image_gun = pygame.image.load(image_gun)
            self.__image_gun = pygame.transform.scale(self.__image_gun, (scale, scale))
            self.__rotated_image = self.__image_gun
            self.__rotated_image_rect = coordinate
        else:
            self.__image_gun = None
            self.__rotated_image = self.__image_gun
        if radius is not None:
            self.__radius = scale / 2 + radius * scale * 1.2
            self.__radius_image = pygame.transform.scale(pygame.image.load('images/UI/highlighting/radius.png'), (self.__radius * 2, self.__radius * 2))
        self.__is_charged = (pygame.transform.scale(pygame.image.load('images/UI/enemyСharacteristic/charged.png'), (self.__scale / 6, self.__scale / 6)),
                             pygame.transform.scale(pygame.image.load('images/UI/enemyСharacteristic/notCharged.png'), (self.__scale / 6, self.__scale / 6)))
        self.__level_image_tuple = (pygame.transform.scale(pygame.image.load('images/upgrade/1lvl.png'), (self.__scale / 4, self.__scale / 4)),
                                    pygame.transform.scale(pygame.image.load('images/upgrade/2lvl.png'), (self.__scale / 4, self.__scale / 4)),
                                    pygame.transform.scale(pygame.image.load('images/upgrade/3lvl.png'), (self.__scale / 4, self.__scale / 4)))



    def is_in_radius(self, context):  # проверяет, в радиусе ли точка
        if ((self.__coordinate[0] + self.__scale / 2 - context.get_enemies_controller().get_current_enemy().get_center()[0]) ** 2 + (self.__coordinate[1] + self.__scale / 2 - context.get_enemies_controller().get_current_enemy().get_center()[1]) ** 2) <= self.__radius**2 and self.__is_used == False:  # если башня не использованная и координаты центра врага в радиусе башни
            return True
        else:
            return False

    def draw_tower(self, context):  # рисует башню на карте
        context.get_config_parameter_scene().get_screen().blit(self.__image_foundation, self.__coordinate)
        if self.__rotated_image is not None:
            context.get_config_parameter_scene().get_screen().blit(self.__rotated_image, self.__rotated_image_rect)
        if context.get_config_gameplay().get_always_use_additional_parameters() or context.get_config_gameplay().get_use_additional_parameters():
            context.get_config_parameter_scene().get_screen().blit(self.__level_image_tuple[self.__level - 1], (self.__coordinate[0] + self.__scale / 8, self.__coordinate[1] + self.__scale / 14))
            if self.__is_used:
                context.get_config_parameter_scene().get_screen().blit(self.__is_charged[1], (self.__coordinate[0], self.__coordinate[1] + self.__scale / 8))
            else:
                context.get_config_parameter_scene().get_screen().blit(self.__is_charged[0], (self.__coordinate[0], self.__coordinate[1] + self.__scale / 8))

    def draw_picture_tower(self, scale, coordinate_center, context):  # рисует башню с заданным размером(нужно для картинки в магазине)
        context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(self.__image_foundation, (scale, scale)), (coordinate_center[0] - scale / 2, coordinate_center[1] - scale / 2))
        if self.__rotated_image is not None:
            __rotated_image = pygame.transform.scale(self.__image_gun, (scale, scale))
            __rotated_image = pygame.transform.rotate(__rotated_image, self.__angle)
            context.get_config_parameter_scene().get_screen().blit(__rotated_image, __rotated_image.get_rect(center = coordinate_center))


    def draw_radius(self, context):  # рисует радиус
        context.get_config_parameter_scene().get_screen().blit(self.__radius_image, (self.__coordinate[0] + self.__scale / 2 - self.__radius, self.__coordinate[1] + self.__scale / 2 - self.__radius))


    def rotate_gun(self):  # поворачивает ствол в сторону мышки
        if not self.__is_used:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = (mouse_x - self.__coordinate[0] - self.__scale / 2), (mouse_y - self.__coordinate[1] - self.__scale / 2)
            self.__angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90 # угол от мышки до координаты башни, деленный на некоторое число для плавной анимации

            rotated_coordinate_center = (self.__coordinate[0] + self.__scale / 2, self.__coordinate[1] + self.__scale / 2)  # координаты центра башни

            self.__rotated_image = pygame.transform.rotate(self.__image_gun, self.__angle)  # вращает башню
            self.__rotated_image_rect = self.__rotated_image.get_rect(center = rotated_coordinate_center)  # получает координату нового центра


    def upgrade(self, increase_damage, increase_radius):  # улучшение башни(увеличивает урон и радиус на заданное значение)
        self.__damage += increase_damage
        self.__radius += increase_radius
        self.__radius_image = pygame.transform.scale(pygame.image.load('images/UI/highlighting/radius.png'), (self.__radius * 2, self.__radius * 2))

    def get_additional_money(self):  # возвращает дополнительные деньги за башню
        return self.__additional_money

    def get_characteristic(self):  # возвращает словарь характеристик и их значений
        characteristic_dict = {'damage': 'damage ' + str(self.__damage), 'radius': 'radius ' + str(round((self.__radius - self.__scale / 2) / (self.__scale * 1.2)))}
        if self.__armor_piercing:
            characteristic_dict['armor'] = 'armor piercing'
        if self.__poison > 0:
            characteristic_dict['poison'] = 'venom ' + str(self.__poison)
        if self.__additional_money > 0:
            characteristic_dict['money'] = 'additional_money ' + str(self.__additional_money)
        return characteristic_dict

    def get_started_coordinate_bullet(self):  # возвращает кортеж координат начального положения пули
        return (math.ceil(self.__coordinate[0] + self.__scale / 2 + self.__scale / 3 * math.cos(math.radians(90 - self.__angle))), math.ceil(self.__coordinate[1] + self.__scale / 2 + self.__scale / 3 * math.sin(math.radians(90 - self.__angle))))

    def get_index(self):  # геттеры
        return self.__index

    def get_damage(self):
        return self.__damage

    def get_poison(self):
        return self.__poison

    def get_armor_piercing(self):
        return self.__armor_piercing

    def set_damage(self, value):
        self.__damage += value

    def get_is_used(self):
        return self.__is_used

    def set_is_used(self, value):
        self.__is_used = value

    def get_image_gun(self):
        return self.__image_gun

    def get_radius(self):
        return self.__radius

    def get_level(self):
        return self.__level

    def set_level(self):
        self.__level += 1

    def get_improve_cost_array(self):
        return self.__improve_cost_array