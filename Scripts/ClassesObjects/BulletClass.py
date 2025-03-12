from pygame import sprite, transform
from math import ceil, atan2, degrees

class Bullet(sprite.Sprite):

    def __init__(self, image, started_coordinate_center, final_coordinate_center, fps):
        sprite.Sprite.__init__(self)
        self.__delta = (ceil((final_coordinate_center[0] - started_coordinate_center[0]) / fps), ceil((final_coordinate_center[1] - started_coordinate_center[1]) / fps))
        self.image = transform.rotate(image, degrees(atan2(self.__delta[0], self.__delta[1])) + 180)
        self.rect = self.image.get_rect()
        self.rect.center = started_coordinate_center
        self.__time_to_destroy = fps

    def update(self):
        self.rect.x += self.__delta[0]
        self.rect.y += self.__delta[1]
        self.__time_to_destroy -= 1
        if self.__time_to_destroy == 0:
            self.kill()