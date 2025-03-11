from pygame import sprite
from math import ceil

class Bullet(sprite.Sprite):

    def __init__(self, image, started_coordinate_center, final_coordinate_center, fps):
        sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.__delta = (ceil((final_coordinate_center[0] - started_coordinate_center[0]) / fps), ceil((final_coordinate_center[1] - started_coordinate_center[1]) / fps))
        self.__final_coordinate_x = started_coordinate_center[0] + self.__delta[0] * fps
        self.__end = False
        self.rect.center = started_coordinate_center

    def update(self):
        self.rect.x += self.__delta[0]
        self.rect.y += self.__delta[1]
        if self.rect.x == self.__final_coordinate_x:
            self.__end = True