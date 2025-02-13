import pygame

class ConfigParameterScreen:

    def __init__(self, width, height):
        self.scene = 'mainMenu'
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_screen(self):
        return self.screen

    def get_scene(self):
        return self.scene

    def new_value_scene(self, new_value):
        self.scene = new_value