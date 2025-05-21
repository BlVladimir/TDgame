import pygame
from scripts.main_scripts.resourse_path import resource_path


class OnlyImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def __copy__(self, scale, coordinate):
        new = self.__class__(pygame.transform.scale(self.image, (scale, scale)), coordinate)
        return new


class TowerConfig:
    def __init__(self):
        self.__products = {
            'common': dict(image="images/tower/common_foundation.png", damage=2, cost=3, radius=1,
                           improve_cost_array=(4, 6), additional_money=2, additional_image="images/tower/common_gun.png"),
            'sniper': dict(image="images/tower/common_foundation.png", damage=4, cost=5, radius=2,
                           improve_cost_array=(6, 8), additional_image="images/tower/sniper_gun.png"),
            'anty_shield': dict(image="images/tower/anty_shield.png", damage=3, cost=4, radius=1.5,
                                improve_cost_array=(5, 7), armor_piercing=True),
            'venom': dict(image="images/tower/venom_foundation.png", damage=2, cost=5, radius=1,
                          improve_cost_array=(4, 6), poison=2, additional_image="images/tower/venom_gun.png")}

        self.__images_bullets_dict = {'poison': 'animation_poison_bullet',
                                      'piercing_armor': 'animation_electric_bullet',
                                      'common': pygame.image.load(resource_path('images/tower/Bullets/common_bullet.png'))}

        self.__is_charged_sprites_tuple = (OnlyImageSprite(pygame.image.load(resource_path('images/UI/enemy_characteristic/charged.png')), (0, 0)),
                                           OnlyImageSprite(pygame.image.load(resource_path('images/UI/enemy_characteristic/not_charged.png')), (0, 0)))  # картинка заряжена башня или нет

        self.__level_image_sprites_tuple = (OnlyImageSprite(pygame.image.load(resource_path('images/upgrade/1lvl.png')), (0, 0)),
                                            OnlyImageSprite(pygame.image.load(resource_path('images/upgrade/2lvl.png')), (0, 0)),
                                            OnlyImageSprite(pygame.image.load(resource_path('images/upgrade/3lvl.png')), (0, 0)))  # картинка уровня башни

        self.__sprites_towers_dict = {
            'common': "images/tower/common_foundation.png",
            'sniper': "images/tower/common_foundation.png",
            'anty_shield': "images/tower/anty_shield.png",
            'venom': "images/tower/venom_foundation.png"
        }

    def get_improve_cost_array(self, type_tower):
        return self.__products[type_tower]['improve_cost_array']

    def get_image_tuple(self, type_tower):
        if 'additional_image' in self.__products[type_tower].key():
            return (self.__products[type_tower]['image'], self.__products[type_tower]['additional_image'])
        else:
            return (self.__products[type_tower]['image'],)

    def get_started_characteristic_dict(self, type_tower):
        r = {}
        for i in ['damage', 'radius', 'armor_piercing', 'poison', 'additional_money']:
            if i in self.__products[type_tower].key():
                r[i] = self.__products[type_tower][i]
        return r

    def get_cost(self, type_tower):
        return self.__products[type_tower]['cost']

    def get_images_bullets(self, type_tower):
        return self.__images_bullets_dict[type_tower]

