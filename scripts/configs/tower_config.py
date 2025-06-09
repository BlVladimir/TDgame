import pygame
from scripts.main_scripts.resourse_path import resource_path
from scripts.classes_objects.bullet_class import Bullet, BulletWithAnimation
from scripts.main_scripts.function import get_images_array_from_directory
from scripts.tower.visitor.visitor_for_upgrade import VisitorForUpgrade

class OnlyImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect:pygame.Rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def clone(self, rect:pygame.Rect):
        new = self.__class__(pygame.transform.scale(self.image, rect.size), rect)
        return new


class GunSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect:pygame.Rect):
        super().__init__()
        self.__started_image = image
        self.image = image
        self.rect = rect

    def rotate_image(self, angle):
        self.image = pygame.transform.rotate(self.__started_image, angle)  # вращает башню
        self.rect = self.image.get_rect(center=self.rect.center)  # получает координату нового центра

    def clone(self, rect):
        new = self.__class__(pygame.transform.scale(self.__started_image, (rect.width, rect.height)), rect)
        return new

class TowerConfig:
    def __init__(self):
        self.__products = {
            'common': dict(damage=2, cost=3, radius=1, improve_cost_array=(4, 6), additional_money=2),
            'sniper': dict(damage=4, cost=5, radius=2, improve_cost_array=(6, 8)),
            'anty_shield': dict(damage=3, cost=4, radius=1.5, improve_cost_array=(5, 7), armor_piercing=True),
            'venom': dict(damage=2, cost=5, radius=1, improve_cost_array=(4, 6), poison=2)}

        self.__images_bullets_dict = {'poison': BulletWithAnimation(get_images_array_from_directory('animation_poison_bullet')),
                                      'piercing_armor': BulletWithAnimation(get_images_array_from_directory('animation_electric_bullet')),
                                      'common': Bullet(pygame.image.load(resource_path('images/tower/Bullets/common_bullet.png')))}

        self.__is_charged_sprites_tuple = (OnlyImageSprite(pygame.image.load(resource_path('images/UI/enemy_characteristic/charged.png')), pygame.Rect((0, 0), (0, 0))),
                                           OnlyImageSprite(pygame.image.load(resource_path('images/UI/enemy_characteristic/not_charged.png')), pygame.Rect((0, 0), (0, 0))))  # картинка заряжена башня или нет

        self.__level_image_sprites_tuple = (OnlyImageSprite(pygame.image.load(resource_path('images/upgrade/1lvl.png')), pygame.Rect((0, 0), (0, 0))),
                                            OnlyImageSprite(pygame.image.load(resource_path('images/upgrade/2lvl.png')), pygame.Rect((0, 0), (0, 0))),
                                            OnlyImageSprite(pygame.image.load(resource_path('images/upgrade/3lvl.png')), pygame.Rect((0, 0), (0, 0))))  # картинка уровня башни

        self.__sprites_towers_foundations_dict = {
            'common': OnlyImageSprite(pygame.image.load(resource_path("images/tower/common_foundation.png")), pygame.Rect((0, 0), (0, 0))),
            'sniper': OnlyImageSprite(pygame.image.load(resource_path("images/tower/common_foundation.png")), pygame.Rect((0, 0), (0, 0))),
            'anty_shield': OnlyImageSprite(pygame.image.load(resource_path("images/tower/anty_shield.png")), pygame.Rect((0, 0), (0, 0))),
            'venom': OnlyImageSprite(pygame.image.load(resource_path("images/tower/venom_foundation.png")), pygame.Rect((0, 0), (0, 0)))}

        self.__sprites_towers_guns_dict = {
            'common': GunSprite(pygame.image.load(resource_path("images/tower/common_gun.png")), pygame.Rect((0, 0), (0, 0))),
            'sniper': GunSprite(pygame.image.load(resource_path("images/tower/sniper_gun.png")), pygame.Rect((0, 0), (0, 0))),
            'venom': GunSprite(pygame.image.load(resource_path("images/tower/venom_gun.png")), pygame.Rect((0, 0), (0, 0)))}

        self.__visitors_dict = {
            'common': VisitorForUpgrade(damage=2, radius=1.2),
            'sniper': VisitorForUpgrade(damage=2, radius=1.2),
            'anty_shield': VisitorForUpgrade(damage=2, radius=1.2),
            'venom': VisitorForUpgrade(damage=2, radius=1.2)}

    def get_visitor_improve(self, type_tower:str):
        return self.__visitors_dict[type_tower]

    def get_improve_cost_array(self, type_tower:str):
        return self.__products[type_tower]['improve_cost_array']

    def get_image_tuple(self, type_tower:str):
        if 'additional_image' in self.__products[type_tower].key():
            return (self.__products[type_tower]['image'], self.__products[type_tower]['additional_image'])
        else:
            return (self.__products[type_tower]['image'],)

    def get_started_characteristic_dict(self, type_tower:str):
        r = {}
        for i in ['damage', 'radius', 'armor_piercing', 'poison', 'additional_money']:
            if i in self.__products[type_tower].key():
                r[i] = self.__products[type_tower][i]
        return r

    def get_cost(self, type_tower:str):
        return self.__products[type_tower]['cost']

    def get_sprite_bullets(self, type_bullet, started_coordinate_center, final_coordinate_center, fps, scale):
        return self.__images_bullets_dict[type_bullet].clone(started_coordinate_center, final_coordinate_center, fps, scale)

    def get_sprite_foundation(self, type_tower:str, rect:pygame.Rect):
        return self.__sprites_towers_foundations_dict[type_tower].clone(rect)

    def get_sprite_gun(self, type_tower:str, rect:pygame.Rect):
        if type_tower in self.__sprites_towers_guns_dict.keys():
            return self.__sprites_towers_guns_dict[type_tower].clone(rect)
        else:
            return None

    @property
    def is_charged_sprites_tuple(self):
        return self.__is_charged_sprites_tuple

    @property
    def level_image_sprites_tuple(self):
        return self.__level_image_sprites_tuple