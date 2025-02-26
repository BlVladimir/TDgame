import pygame

from Scripts.ClassesObjects.InformationClass import Information
from Scripts.ClassesObjects.ButtonClass import Button


class ConfigConstantObject:

    def __init__(self, height, width, action_exit, action_scene, change_using_additional_parameter):
        self.__clock = pygame.time.Clock()
        self.__information_table = Information(height, width)
        self.__button_exit = Button(width - 170 - height * 0.4, 20, "images/UI/exit.png", 150, 75, action_exit)
        self.__button_main_manu = Button(150, 20, "images/UI/exitInMainManu.png", 100, 100, action_scene)
        self.__button_setting = Button(20, 20, "images/UI/settings.png", 100, 100, action_scene)  # объекты кнопок
        self.__button_additional_parameter = Button(width / 2, height / 2, 'images/UI/satingButtonTrue.png', 150, 150, change_using_additional_parameter)
        self.__button_level_array = (Button(width / 2 - 600, height / 2 - 300, "images/UI/lvl/lvl1.png", 300, 300, action_scene),
                                     Button(width / 2 - 200, height / 2 - 300, "images/UI/lvl/lvl2.png", 300, 300, action_scene),
                                     Button(width / 2 + 200, height / 2 - 300, "images/UI/lvl/lvl3.png", 300, 300, action_scene),
                                     Button(width / 2 - 600, height / 2 + 100, "images/UI/lvl/lvl4.png", 300, 300, action_scene),
                                     Button(width / 2 - 200, height / 2 + 100, "images/UI/lvl/lvl5.png", 300, 300, action_scene),
                                     Button(width / 2 + 200, height / 2 + 100, "images/UI/lvl/lvl6.png", 300, 300, action_scene))

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

    def get_button_additional_parameter(self):
        return self.__button_additional_parameter