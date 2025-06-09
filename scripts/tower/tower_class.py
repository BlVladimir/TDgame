import pygame  # импорт библиотеки pygame

from pygame.examples.cursors import image

class OnlyImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect:pygame.Rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def __copy__(self, rect:pygame.Rect):
        new = self.__class__(pygame.transform.scale(self.image, rect.size), rect)
        return new

class TowerSpritesGroup:
    def __init__(self, type_tower, rect:pygame.Rect, context, gun_sprite=None):
        self.__sprites_group = pygame.sprite.Group(context.tower_config.get_sprite_foundation(type_tower, rect))
        if gun_sprite:
            self.__sprites_group.add(gun_sprite)
        self.__rect = rect

    def update(self):
        self.__sprites_group.update()

    def update_state_group(self, level, is_charged, context):
        for i in context.tower_config.is_charged_sprites_tuple:
            if self.__sprites_group.has(i):
                self.__sprites_group.remove(i)
        for i in context.tower_config.level_image_sprites_tuple:
            if self.__sprites_group.has(i):
                self.__sprites_group.remove(i)
        if context.config_gameplay.get_always_use_additional_parameters() or context.config_gameplay.get_use_additional_parameters():
            self.__sprites_group.add(context.tower_config.is_charged_sprites_tuple[int(is_charged)])
            self.__sprites_group.add(context.tower_config.level_image_sprites_tuple[level-1])

    def draw(self, context):
            self.__sprites_group.draw(context.config_parameter_scene.get_screen())

    @property
    def center(self):
        return self.__rect.center

    @property
    def bullet_scale(self):
        return self.__rect.width * 0.05

class Tower:
    # инициализация класса
    def __init__(self, type_tower:str, rect:pygame.Rect, index, improve_cost_array, damage_state, gun_strategy, radius_strategy):
        self.__type_tower = type_tower

        self.__damage_state = damage_state
        self.__gun_strategy = gun_strategy
        self.__radius_strategy = radius_strategy
        self.__tower_sprites_group = TowerSpritesGroup(image, rect, self.__gun_strategy.gun_sprite)

        self.__is_used = False  # башня выстрелила или нет
        self.__index = index  # индекс, совпадает с номером тайла
        self.__level = 1  # уровень башни
        self.__improve_cost_array = improve_cost_array  # массив цен улучшения

    def push(self, context):
        context.tower_config.get_sprite_bullets(self.__damage_state._type_bullet, self.__tower_sprites_group.center, context.enemies_array_controller.get_current_enemy().get_center(), context.config_gameplay.get_fps(), self.__tower_sprites_group.bullet_scale)
        self.__damage_state.push(context.enemies_array_controller.get_current_enemy())

    def draw_tower(self, context):  # рисует башню на карте
        self.__tower_sprites_group.update()
        self.__tower_sprites_group.draw(context.config_parameter_scene.get_screen())

    def upgrade(self, context):
        self.__damage_state.upgrade(context.tower_config.get_visitor_improve(self.__type_tower))