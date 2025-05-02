import pygame
from scripts.classes_objects.information_class import Information
from scripts.classes_objects.shop_class import Shop


class ConfigConstantObject:

    def __init__(self, height, width, highlighting):
        self.__clock = pygame.time.Clock()
        self.__information_table = Information(height, width)
        self.__shop = Shop(height)
        self.__highlighting = highlighting

    def get_clock(self):
        return self.__clock

    def get_information_table(self):
        return self.__information_table

    @property
    def shop(self):
        return self.__shop

    @property
    def highlighting(self):
        return self.__highlighting