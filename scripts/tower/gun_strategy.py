import pygame
import math
from scripts.main_scripts.resourse_path import resource_path
class GunSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def change_image(self, new_image, new_rect):
        self.image = new_image
        self.rect = new_rect

class CommonGunStrategy:
    def __init__(self, image, scale, rect):
        self.__image = pygame.transform.scale(pygame.image.load(resource_path(image)), (scale, scale))
        self.__rect = pygame.rect.Rect(rect, (scale, scale))
        self.__rotated_image = self.__image
        self.__angle = 0
        self.__sprite = GunSprite(self.__image, rect)

    def rotate_gun(self):  # поворачивает ствол в сторону мышки
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = (mouse_x - self.__rect.center[0]), (mouse_y - self.__rect.center[1])
        self.__angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90 # угол от мышки до координаты башни, деленный на некоторое число для плавной анимации

        rotated_image = pygame.transform.rotate(self.__image, self.__angle)  # вращает башню
        rotated_rect = self.__rotated_image.get_rect(center = self.__rect.center)  # получает координату нового центра
        self.__sprite.change_image(rotated_image, rotated_rect)

    @property
    def gun_sprite(self):
        return self.__sprite

class NullGunStrategy:
    def rotate_gun(self):
        pass

    @property
    def gun_sprite(self):
        return None