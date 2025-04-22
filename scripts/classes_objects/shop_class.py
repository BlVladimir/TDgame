import pygame
from scripts.main_scripts import function
from scripts.classes_objects.product_class import Product
from scripts.classes_objects.information_class import get_coordinate_list
from scripts.main_scripts.resourse_path import resource_path

pygame.init()

class Shop:

    def __init__(self, height):
        self.__money_picture = pygame.transform.scale(pygame.image.load(resource_path('images/UI/money.png')), (height * 0.1, height * 0.1))  # картинка монеты
        self.__image_shop = pygame.transform.scale(pygame.image.load(resource_path('images/UI/shop_background.png')), (height * 0.4, height))  # картинка фона для магазина
        self.__products = [Product("images/tower/common_foundation.png", 3, height * 0.1, (20, 150), 2, 1, (4, 6), False, 0, "images/tower/common_gun.png"),  # coordinate = (20, 150 + i * 120)
                           Product("images/tower/sniper_foundation.png", 5, height * 0.1, (20, 270), 4, 2, (6, 8), False, 0, "images/tower/sniper_gun.png"),
                           Product("images/tower/anty_shield.png", 4, height * 0.1, (20, 390), 3, 1.5, (5, 7), True, 0),
                           Product("images/tower/venom_foundation.png", 5, height * 0.1, (20, 510), 2, 1, (6, 8), False, 2, "images/tower/venom_gun.png")]  # объекты продуктов
        self.__image_characteristic_dict = {'damage': pygame.image.load(resource_path('images/UI/up/damage_up_up.png')),
                                            'radius': pygame.image.load(resource_path('images/UI/up/radius_up_up.png')),
                                            'armor': pygame.image.load(resource_path('images/UI/up/anty_shield_up.png')),
                                            'poison': pygame.image.load(resource_path('images/UI/up/poison_up_up.png')),
                                            'money': pygame.image.load(resource_path('images/UI/up/money_up_up.png'))}  # картинки характеристик башни

        self.__scale_products = height * 0.1  # размер кнопок продуктов
        for i in self.__image_characteristic_dict.keys():
            self.__image_characteristic_dict[i] = pygame.transform.scale(self.__image_characteristic_dict[i], (height * 0.08, height * 0.08))  # меняет размеры всем характеристикам


    def draw(self, towers_controller, context): #  рисует магазин
        if context.get_config_gameplay().get_shop_type() == 1:
            self.__draw_store(context)
            for i in self.__products:
                i.draw(context)
        elif context.get_config_gameplay().get_shop_type() == 2:
            self.__draw_up(towers_controller, context)

    def __draw_up(self, towers_controller, context):  # рисует кнопку улучшения
        height = context.get_config_parameter_scene().get_height()
        context.get_config_parameter_scene().get_screen().blit(self.__image_shop, (0, 0))
        if towers_controller.get_current_tower() is not None:
            towers_controller.get_current_tower().draw_picture_tower(height * 0.16, (height * 0.2, 200), context)
            self.__draw_tower_parameter(context)
            towers_controller.get_current_button_update().draw(context)

    def __draw_store(self, context): #  проходится по массиву возможных покупок и рисует магазин
        context.get_config_parameter_scene().get_screen().blit(self.__image_shop, (0, 0))
        for i in self.__products:
            function.draw_text('x' + str(i.get_cost()), 100, (i.get_product_coordinate()[0] + self.__scale_products * 1.5, i.get_product_coordinate()[1] + self.__scale_products * 0.5), context)
            context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(self.__money_picture, (self.__scale_products * 0.9, self.__scale_products * 0.9)), (i.get_product_coordinate()[0] + self.__scale_products * 2.1, i.get_product_coordinate()[1] + self.__scale_products * 0.1))

    def __draw_tower_parameter(self, context):  # рисует характеристики башни
        height = context.get_config_parameter_scene().get_height()
        if context.get_towers_controller().get_current_tower() is not None:
            characteristic_dict = context.get_towers_controller().get_current_tower().get_characteristic()
            coordinate_array = get_coordinate_list(height * 0.38, height * 0.5, len(characteristic_dict), (0, height * 0.16), 1)
            i = 0
            for j in characteristic_dict.keys():
                context.get_config_parameter_scene().get_screen().blit(self.__image_characteristic_dict[j], (coordinate_array[i][0] + context.get_config_parameter_scene().get_height() * 0.06, coordinate_array[i][1] - context.get_config_parameter_scene().get_height() * 0.02))
                function.draw_text(characteristic_dict[j], int(context.get_config_parameter_scene().get_height() * 0.06), (coordinate_array[i][0] + context.get_config_parameter_scene().get_height() * 0.15, coordinate_array[i][1]), context, 1)
                i += 1


    def build_tower(self, event, context):  # проверяет, нажата ли кнопка продуктов и покупает башню
        mouse_pose = pygame.mouse.get_pos()
        current_tile = context.get_config_gameplay().get_current_tile()
        if current_tile is not None:
            for i in self.__products:
                if i.get_coordinate()[0] < mouse_pose[0] < i.get_coordinate()[0] + i.get_scale() and i.get_coordinate()[0] < mouse_pose[0] < i.get_coordinate()[0] + i.get_scale():
                    context.get_maps_controller().get_build_array()[current_tile]['is_filled'] = i.buy(event, context)
                    if context.get_maps_controller().get_build_array()[current_tile]['is_filled']:
                        break

    def get_money_picture(self):  # возвращает картинку монеты
        return self.__money_picture
