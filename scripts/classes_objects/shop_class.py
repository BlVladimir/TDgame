import pygame
from scripts.main_scripts import function
from scripts.classes_objects.information_class import get_coordinate_list

pygame.init()

class Shop(pygame.sprite.Sprite):

    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.__money_picture = pygame.transform.scale(pygame.image.load('images/UI/money.png'), (height * 0.1, height * 0.1))
        self.__tower_characteristic_image = (pygame.transform.scale(pygame.image.load('images/UI/up/damage_up_up.png'), (100, 100)),
                                           pygame.transform.scale(pygame.image.load('images/UI/up/radius_up_up.png'), (100, 100)))
        self.__image_characteristic_dict = {'damage': pygame.image.load('images/UI/up/damage_up_up.png'),
                                            'radius': pygame.image.load('images/UI/up/radius_up_up.png'),
                                            'armor': pygame.image.load('images/UI/up/anty_shield_up.png'),
                                            'poison': pygame.image.load('images/UI/up/poison_up_up.png'),
                                            'money': pygame.image.load('images/UI/up/money_up_up.png')}
        self.image = pygame.transform.scale(pygame.image.load('images/UI/shop_background.png'), (height * 0.4, height))  # картинка
        self.rect = (0, 0)
        for i in self.__image_characteristic_dict.keys():
            self.__image_characteristic_dict[i] = pygame.transform.scale(self.__image_characteristic_dict[i], (height * 0.08, height * 0.08))


    def draw(self, towers_array_iterator, context): #  рисует магазин
        if context.config_gameplay.get_shop_type()== 2:
            self.__draw_up(towers_array_iterator, context)
            context.buttons_groups_controller.deactivate_products_group()
        elif context.config_gameplay.get_shop_type()== 1:
            context.buttons_groups_controller.activate_products_group()
        else:
            context.buttons_groups_controller.deactivate_products_group()

    def __draw_up(self, towers_array_iterator, context):  # рисует кнопку улучшения
        height = context.config_parameter_scene.get_height
        if towers_array_iterator.get_current_tower() is not None:
            towers_array_iterator.get_current_tower().draw_picture_tower(height * 0.16, (height * 0.2, 200), context)
            self.__draw_tower_parameter(context)

    def __draw_tower_parameter(self, context):  # рисует характеристики башни
        height = context.config_parameter_scene.get_height
        if context.towers_array_iterator.get_current_tower()is not None:
            characteristic_dict = context.towers_array_iterator.get_current_tower.get_characteristic()
            coordinate_array = get_coordinate_list(height * 0.38, height * 0.5, len(characteristic_dict), (0, height * 0.16), 1)
            i = 0
            for j in characteristic_dict.keys():
                context.config_parameter_scene.get_screen().blit(self.__image_characteristic_dict[j], (coordinate_array[i][0] + context.config_parameter_scene.get_height()* 0.06, coordinate_array[i][1] - context.config_parameter_scene.get_height()* 0.02))
                function.draw_text(characteristic_dict[j], int(context.config_parameter_scene.get_height()* 0.06), (coordinate_array[i][0] + context.config_parameter_scene.get_height()* 0.15, coordinate_array[i][1]), context, 1)
                i += 1

    def get_money_picture(self):  # возвращает картинку монеты
        return self.__money_picture
