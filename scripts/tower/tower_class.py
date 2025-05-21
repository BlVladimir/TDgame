import pygame  # импорт библиотеки pygame
import math

from pygame.examples.cursors import image

from scripts.main_scripts.resourse_path import resource_path

class OnlyImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def __copy__(self, scale, coordinate):
        new = self.__class__(pygame.transform.scale(self.image, (scale, scale)), coordinate)
        return new

class TowerSpritesGroup:
    def __init__(self, image, coordinate, scale, gun_sprite):
        self.__sprites_group = pygame.sprite.Group(OnlyImageSprite(pygame.transform.scale(pygame.image.load(resource_path(image)),(scale, scale)), coordinate))
        if gun_sprite:
            self.__sprites_group.add(gun_sprite)
        self.__rect = pygame.rect.Rect(coordinate, (scale, scale))
        self.__is_charged_sprites_tuple = (OnlyImageSprite(pygame.transform.scale(pygame.image.load(resource_path('images/UI/enemy_characteristic/charged.png')), (scale / 6, scale / 6)), coordinate),
                                           OnlyImageSprite(pygame.transform.scale(pygame.image.load(resource_path('images/UI/enemy_characteristic/not_charged.png')), (scale / 6, scale / 6)), coordinate))  # картинка заряжена башня или нет
        self.__level_image_sprites_tuple = (OnlyImageSprite(pygame.transform.scale(pygame.image.load(resource_path('images/upgrade/1lvl.png')), (scale / 4, scale / 4)), coordinate),
                                            OnlyImageSprite(pygame.transform.scale(pygame.image.load(resource_path('images/upgrade/2lvl.png')), (scale / 4, scale / 4)), coordinate),
                                            OnlyImageSprite(pygame.transform.scale(pygame.image.load(resource_path('images/upgrade/3lvl.png')), (scale / 4, scale / 4)), coordinate))  # картинка уровня башни

    def update(self):
        self.__sprites_group.update()

    def update_state_group(self, level, is_charged, context):
        for i in self.__is_charged_sprites_tuple:
            if self.__sprites_group.has(i):
                self.__sprites_group.remove(i)
        for i in self.__level_image_sprites_tuple:
            if self.__sprites_group.has(i):
                self.__sprites_group.remove(i)
        if context.config_gameplay.get_always_use_additional_parameters() or context.config_gameplay.get_use_additional_parameters():
            self.__sprites_group.add(self.__is_charged_sprites_tuple[int(is_charged)])
            self.__sprites_group.add(self.__is_charged_sprites_tuple[level-1])

    def draw(self, context):
            self.__sprites_group.draw(context.config_parameter_scene.get_screen())

class Tower:
    # инициализация класса
    def __init__(self, image_foundation, scale, coordinate, index, improve_cost_array, damage_state, gun_strategy, radius_strategy):
        self.__damage_state = damage_state
        self.__gun_strategy = gun_strategy
        self.__radius_strategy = radius_strategy
        self.__tower_sprites_group = TowerSpritesGroup(image, coordinate, scale, self.__gun_strategy.gun_sprite)
        self.__is_used = False  # башня выстрелила или нет
        self.__index = index  # индекс, совпадает с номером тайла
        self.__level = 1  # уровень башни
        self.__improve_cost_array = improve_cost_array  # массив цен улучшения

    def draw_tower(self, context):  # рисует башню на карте
        self.__tower_sprites_group.update()
        self.__tower_sprites_group.draw(context.config_parameter_scene.get_screen())

    def upgrade(self, increase_damage, increase_radius):  # улучшение башни(увеличивает урон и радиус на заданное значение)
        self.__damage += increase_damage
        self.__radius += increase_radius

    def get_characteristic(self):  # возвращает словарь характеристик и их значений
        characteristic_dict = {'damage': 'damage ' + str(self.__damage), 'radius': 'radius ' + str(round((self.__radius - self.__scale / 2) / (self.__scale * 1.2)))}
        if self.__armor_piercing:
            characteristic_dict['armor'] = 'armor piercing'
        if self.__poison > 0:
            characteristic_dict['poison'] = 'venom ' + str(self.__poison)
        if self.__additional_money > 0:
            characteristic_dict['money'] = 'additional_money ' + str(self.__additional_money)
        return characteristic_dict

    def get_started_coordinate_bullet(self):  # возвращает кортеж координат начального положения пули
        if self.__rotated_image is not None:
            return (math.ceil(self.__coordinate[0] + self.__scale / 2 + self.__scale / 3 * math.cos(math.radians(90 - self.__angle))), math.ceil(self.__coordinate[1] + self.__scale / 2 + self.__scale / 3 * math.sin(math.radians(90 - self.__angle))))
        else:
            return (self.__coordinate[0] + self.__scale / 2, self.__coordinate[1] + self.__scale / 2)

    def get_index(self):  # геттеры
        return self.__index

    def get_damage(self):
        return self.__damage

    def get_poison(self):
        return self.__poison

    def get_armor_piercing(self):
        return self.__armor_piercing

    def set_damage(self, value):
        self.__damage += value

    def get_is_used(self):
        return self.__is_used

    def set_is_used(self, value):
        self.__is_used = value

    def get_image_gun(self):
        return self.__image_gun

    def get_radius(self):
        return self.__radius

    def get_level(self):
        return self.__level

    def set_level(self):
        self.__level += 1

    def get_improve_cost_array(self):
        return self.__improve_cost_array