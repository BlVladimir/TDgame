import pygame
from math import ceil, atan2, degrees

class Bullet(pygame.sprite.Sprite):  # наследование от спрайта

    def __init__(self, image, started_coordinate_center = (0, 0), final_coordinate_center = (0, 0), fps = 1):
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

    def clone(self, started_coordinate_center, final_coordinate_center, fps, scale):
        new = self.__class__(pygame.transform.scale(self.image, (scale, scale)), started_coordinate_center, final_coordinate_center, fps)
        return new

class BulletWithAnimation(Bullet):
    def __init__(self, images_array, started_coordinate_center = (0, 0), final_coordinate_center = (0, 0), fps = 1):
        Bullet.__init__(self, images_array[0], started_coordinate_center, final_coordinate_center, fps)
        self.__animation = images_array

    def update(self):
        self.image = pygame.transform.rotate(self.__animation[Bullet.get_time_to_destroy(self) % len(self.__animation)], degrees(atan2(Bullet.get_delta(self)[0], Bullet.get_delta(self)[1])) + 180)  # меняет картинку в зависимости от кадра
        Bullet.update(self)

    def clone(self, started_coordinate_center, final_coordinate_center, fps, scale):
        for i in range(len(self.__animation)):
            self.__animation[i] = pygame.transform.scale(self.__animation[i], (scale, scale))
        new = self.__class__(self.__animation, started_coordinate_center, final_coordinate_center, fps)
        return new