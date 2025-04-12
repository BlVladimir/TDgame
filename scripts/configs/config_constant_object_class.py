import pygame
from math import ceil
from scripts.classes_objects.information_class import Information
from scripts.classes_objects.button_class import Button


class ConfigConstantObject:

    def __init__(self, height, width, action_exit, action_scene):
        self.__clock = pygame.time.Clock()
        self.__information_table = Information(height, width)
        self.__button_exit = Button(width - 170 - height * 0.4, 20, "images/UI/exit.png", 150, 75, action_exit)
        self.__button_main_manu = Button(150, 20, "images/UI/exit_in_main_menu.png", 100, 100, action_scene)
        self.__button_setting = Button(20, 20, "images/UI/settings.png", 100, 100, action_scene)  # объекты кнопок
        if height / 2.5 > width / 4:
            button_level_scale = ceil(width / 4)
        else:
            button_level_scale = ceil(height / 2.5)
        self.__button_level_array = (Button(width / 2 - button_level_scale * 1.5 - height / 20, height / 2 - button_level_scale - height / 40, "images/UI/lvl/lvl1.png", button_level_scale, button_level_scale, action_scene),
                                     Button(width / 2 - button_level_scale / 2, height / 2 - button_level_scale - height / 40, "images/UI/lvl/lvl2.png", button_level_scale, button_level_scale, action_scene),
                                     Button(width / 2 + button_level_scale / 2 + height / 20, height / 2 - button_level_scale - height / 40, "images/UI/lvl/lvl3.png", button_level_scale, button_level_scale, action_scene),
                                     Button(width / 2 - button_level_scale * 1.5 - height / 20, height / 2 + height / 40, "images/UI/lvl/lvl4.png", button_level_scale, button_level_scale, action_scene),
                                     Button(width / 2 - button_level_scale / 2, height / 2 + height / 40, "images/UI/lvl/lvl5.png", button_level_scale, button_level_scale, action_scene),
                                     Button(width / 2 + button_level_scale / 2 + height / 20, height / 2 + height / 40, "images/UI/lvl/lvl6.png", button_level_scale, button_level_scale, action_scene))
        self.__spites = pygame.sprite.Group()

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
        self.__spites.add(new_sprite)

    def update_sprite(self, context):
        self.__spites.update()
        self.__spites.draw(context.config_parameter_scene.get_screen())

    def clear_sprites(self):
        self.__spites.empty()