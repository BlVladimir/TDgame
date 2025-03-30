import pygame
from math import ceil, atan2, degrees
from os import listdir

class Bullet(pygame.sprite.Sprite):  # наследование от спрайта

    def __init__(self, image, started_coordinate_center, final_coordinate_center, fps):
        pygame.sprite.Sprite.__init__(self)
        self.__delta = (ceil((final_coordinate_center[0] - started_coordinate_center[0]) / fps), ceil((final_coordinate_center[1] - started_coordinate_center[1]) / fps))  # кортеж координат вектора перемещения
        self.image = pygame.transform.rotate(image, degrees(atan2(self.__delta[0], self.__delta[1])) + 180)  # картинка
        self.rect = self.image.get_rect()  # координата левого верхнего угла пули
        self.rect.center = started_coordinate_center  # координата центра пули
        self.__time_to_destroy = fps  # количество кадров, через которое пуля долетит до конечно точки

    def update(self):  # изменение координаты пули, и ее уничтожение при достижении конечной точки
        self.rect.x += self.__delta[0]
        self.rect.y += self.__delta[1]
        self.__time_to_destroy -= 1
        if self.__time_to_destroy == 0:
            self.kill()

    def get_time_to_destroy(self):
        return self.__time_to_destroy

    def get_delta(self):
        return self.__delta

class BulletWithAnimation(Bullet):
    def __init__(self, image, started_coordinate_center, final_coordinate_center, fps, animation_directory, scale):
        Bullet.__init__(self, image, started_coordinate_center, final_coordinate_center, fps)
        files_animation = listdir('images/tower/Bullets/' + animation_directory + '/')
        self.__animation = []
        for i in files_animation:
            self.__animation.append(pygame.transform.scale(pygame.image.load('images/tower/Bullets/' + animation_directory + '/' + i), (scale, scale)))

    def update(self):
        self.image = pygame.transform.rotate(self.__animation[Bullet.get_time_to_destroy(self) % len(self.__animation)], degrees(atan2(Bullet.get_delta(self)[0], Bullet.get_delta(self)[1])) + 180)  # картинка
        Bullet.update(self)