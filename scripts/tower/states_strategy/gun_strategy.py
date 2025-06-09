import pygame
import math

class CommonGunStrategy:
    def __init__(self, sprite):
        self.__sprite = sprite

    def rotate_gun(self):  # поворачивает ствол в сторону мышки
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = (mouse_x - self.__sprite.rect.center[0]), (mouse_y - self.__sprite.rect.center[1])
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90 # угол от мышки до координаты башни, деленный на некоторое число для плавной анимации

        self.__sprite.rotate_image(angle)

    @property
    def gun_sprite(self):
        return self.__sprite

class NullGunStrategy:
    def rotate_gun(self):
        pass

    @property
    def gun_sprite(self):
        return None