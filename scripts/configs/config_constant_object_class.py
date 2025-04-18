import pygame
from math import ceil
from scripts.classes_objects.information_class import Information
from scripts.classes_objects.button_class import Button
from scripts.classes_objects.shop_class import Shop


class ConfigConstantObject:

    def __init__(self, height, width, action_exit, action_scene):
        self.__clock = pygame.time.Clock()
        self.__information_table = Information(height, width)
        self.__spites_UI_group = pygame.sprite.Group()
        self.__shop = Shop(height)

    def get_clock(self):
        return self.__clock

    def get_button_level_array(self):
        return self.__button_level_array

    def get_information_table(self):
        return self.__information_table

    def get_button_exit(self):
        return self.__button_exit

    def get_button_main_manu(self):
        return self.__button_main_manu

    def get_button_setting(self):
        return self.__button_setting

    def add_at_sprite(self, new_sprite):
        self.__spites_UI_group.add(new_sprite)

    def update_sprite(self, context):
        self.__spites_UI_group.update()
        self.__spites_UI_group.draw(context.config_parameter_scene.get_screen())

    def clear_sprites(self):
        self.__spites_UI_group.empty()
        self.__spites_UI_group.add(self.__shop)

    @property
    def shop(self):
        return self.__shop