import pygame

class ConfigParameterScreen:

    def __init__(self, width, height):
        self.__scene = 'mainMenu'
        self.__screen = pygame.display.set_mode((width, height))
        self.__width = width
        self.__height = height
        self.__tile_scale = height * 0.1

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_screen(self):
        return self.__screen

    def get_tile_scale(self):
        return self.__tile_scale

    def get_scene(self):
        return self.__scene

    def set_scene(self, new_value):
        self.__scene = new_value