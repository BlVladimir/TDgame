import pygame  # импорт библиотеки pygame
import math
import os


class Tower:
    # инициализация класса
    def __init__(self, image_foundation, scale, damage, coordinate, index, improve_cost_array, armor_piercing, poison, additional_money = 0, image_gun = None, radius = None):
        self.is_used = False
        self.index = index
        self.__image_foundation = pygame.image.load(image_foundation)
        self.__image_foundation = pygame.transform.scale(self.__image_foundation, (scale, scale))
        self.damage = damage
        self.scale = scale
        self.__coordinate = coordinate
        self.angle = 0
        self.armor_piercing = armor_piercing
        self.poison = poison
        self.level = 1
        self.improve_cost_array = improve_cost_array
        self.__additional_money = additional_money
        print(image_gun)
        if image_gun is not None:
            self.image_gun = pygame.image.load(image_gun)
            self.image_gun = pygame.transform.scale(self.image_gun, (scale, scale))
            self.__rotated_image = self.image_gun
            self.__rotated_image_rect = coordinate
        else:
            self.image_gun = None
            self.__rotated_image = self.image_gun
        if radius is not None:
            self.radius = radius
            self.__radius_image = pygame.transform.scale(pygame.image.load('images/UI/highlighting/radius.png'), (radius * 2, radius * 2))
        self.__is_charged = (pygame.transform.scale(pygame.image.load('images/UI/enemyСharacteristic/charged.png'), (self.scale / 6, self.scale / 6)),
                             pygame.transform.scale(pygame.image.load('images/UI/enemyСharacteristic/notCharged.png'), (self.scale / 6, self.scale / 6)))
        self.level_image_tuple = (pygame.transform.scale(pygame.image.load('images/upgrade/1lvl.png'), (self.scale / 4, self.scale / 4)),
                                  pygame.transform.scale(pygame.image.load('images/upgrade/2lvl.png'), (self.scale / 4, self.scale / 4)),
                                  pygame.transform.scale(pygame.image.load('images/upgrade/3lvl.png'), (self.scale / 4, self.scale / 4)))



    def is_in_radius(self, context):
        if ((self.__coordinate[0] + self.scale / 2 - context.get_enemies_controller().get_current_enemy().get_center()[0]) ** 2 + (self.__coordinate[1] + self.scale / 2 - context.get_enemies_controller().get_current_enemy().get_center()[1]) ** 2) <= self.radius**2 and self.is_used == False:  # если башня не использованная и координаты центра врага в радиусе башни
            return True
        else:
            return False

    def draw_tower(self, context):
        context.get_config_parameter_scene().get_screen().blit(self.__image_foundation, self.__coordinate)
        if self.__rotated_image is not None:
            context.get_config_parameter_scene().get_screen().blit(self.__rotated_image, self.__rotated_image_rect)
        if context.get_config_gameplay().get_always_use_additional_parameters() or context.get_config_gameplay().get_use_additional_parameters():
            context.get_config_parameter_scene().get_screen().blit(self.level_image_tuple[self.level - 1], (self.__coordinate[0] + self.scale / 8, self.__coordinate[1] + self.scale/14))
            if self.is_used:
                context.get_config_parameter_scene().get_screen().blit(self.__is_charged[1], (self.__coordinate[0], self.__coordinate[1] + self.scale / 8))
            else:
                context.get_config_parameter_scene().get_screen().blit(self.__is_charged[0], (self.__coordinate[0], self.__coordinate[1] + self.scale / 8))

    def draw_picture_tower(self, scale, coordinate_center, context):
        context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(self.__image_foundation, (scale, scale)), (coordinate_center[0] - scale / 2, coordinate_center[1] - scale / 2))
        if self.__rotated_image is not None:
            __rotated_image = pygame.transform.scale(self.image_gun, (scale, scale))
            __rotated_image = pygame.transform.rotate(__rotated_image, self.angle)
            context.get_config_parameter_scene().get_screen().blit(__rotated_image, __rotated_image.get_rect(center = coordinate_center))


    def draw_radius(self, context):
        context.get_config_parameter_scene().get_screen().blit(self.__radius_image, (self.__coordinate[0] + self.scale / 2 - self.radius, self.__coordinate[1] + self.scale / 2 - self.radius))


    def rotate_gun(self):
        if not self.is_used:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            rel_x, rel_y = (mouse_x - self.__coordinate[0] - self.scale / 2), (mouse_y - self.__coordinate[1] - self.scale / 2)
            self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90 # угол от мышки до координаты башни, деленный на некоторое число для плавной анимации

            rotated_coordinate_center = (self.__coordinate[0] + self.scale / 2, self.__coordinate[1] + self.scale / 2)  # координаты центра башни

            self.__rotated_image = pygame.transform.rotate(self.image_gun, self.angle)  # вращает башню
            self.__rotated_image_rect = self.__rotated_image.get_rect(center = rotated_coordinate_center)  # получает координату нового центра


    def upgrade(self, increase_damage, increase_radius):
        self.damage += increase_damage
        self.radius += increase_radius
        self.__radius_image = pygame.transform.scale(pygame.image.load('images/UI/highlighting/radius.png'), (self.radius * 2, self.radius * 2))

    def get_additional_money(self):
        return self.__additional_money



