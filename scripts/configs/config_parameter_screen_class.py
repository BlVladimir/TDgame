import pygame

class ConfigParameterScreen:

    def __init__(self):
        self.__scene = 'main_menu'
        self.__screen = pygame.display.set_mode()
        self.__width = self.__screen.get_width()
        self.__height = self.__screen.get_height()

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_screen(self):
        return self.__screen

    def get_scene(self):
        return self.__scene

    def set_scene(self, new_value):
        self.__scene = new_value