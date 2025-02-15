import pygame
import Function
from ProductClass import Product

pygame.init()

class Shop:

    def __init__(self, height):
        self.money_picture = pygame.transform.scale(pygame.image.load('images/UI/money.png'), (height * 0.1, height * 0.1))
        self.image_shop = pygame.transform.scale(pygame.image.load('images/UI/shopBackground.png'), (1000 * 0.4, 1000))
        self.tower_characteristic_image = (pygame.transform.scale(pygame.image.load('images/UI/up/damageUpUp.png'), (100, 100)),
                                           pygame.transform.scale(pygame.image.load('images/UI/up/radiusUpUp.png'), (100, 100)))
        self.products = [Product("images/tower/commonFoundation.png", 3, height * 0.1, (20, 150), 2, 170, (4, 6), False, 0, "images/tower/commonGun.png"),  # coordinate = (20, 150 + i * 120)
                         Product("images/tower/sniperFoundation.png", 5, height * 0.1, (20, 270), 4, 230, (6, 8), False, 0, "images/tower/sniperGun.png"),
                         Product("images/tower/antyShield.png", 4, height * 0.1, (20, 390), 3, 200, (5, 7), True, 0),
                         Product("images/tower/venomFoundation.png", 5, height * 0.1, (20, 510), 2, 170, (6, 8), False, 2, "images/tower/venomGun.png")]

        self.scale_products = height * 0.1


    def draw(self, context): #  рисует магазин
        if context.get_config_gameplay().get_shop_type() == 1:
            self.__draw_store(context)
            for i in self.products:
                i.draw(context)
        elif context.get_config_gameplay().get_shop_type() == 2:
            self.__draw_up(context)


    def __draw_up(self, context):  # рисует кнопку улучшения
        height = context.get_config_parameter_scene().get_height()
        towers_object_array = context.get_config_gameplay().get_towers_object_array()
        context.get_config_parameter_scene().get_screen().blit(self.image_shop, (0, 0))
        Function.define_current_tower(context)
        current_tower = context.get_config_gameplay().get_current_tower()
        if current_tower is not None:
            damage_count = towers_object_array[current_tower].damage
            radius_value = round((towers_object_array[current_tower].radius - 50) / 120, 2)
            towers_object_array[current_tower].draw_picture_tower(height * 0.16, (height * 0.2, 200), context)
            self.__draw_tower_parameter(self.tower_characteristic_image[0], 0, damage_count, height, context)
            self.__draw_tower_parameter(self.tower_characteristic_image[1], 1, radius_value, height, context, ' tile')
            context.get_config_gameplay().get_button_update_array()[current_tower].draw(context)

    def __draw_store(self, context): #  проходится по массиву возможных покупок и рисует магазин
        context.get_config_parameter_scene().get_screen().blit(self.image_shop, (0, 0))
        for i in self.products:
            Function.draw_text('x' + str(i.cost), 100, (i.coordinate[0] + self.scale_products * 1.5, i.coordinate[1] + self.scale_products * 0.5), context)
            context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(self.money_picture, (self.scale_products * 0.9, self.scale_products * 0.9)), (i.coordinate[0] + self.scale_products * 2.1, i.coordinate[1] + self.scale_products * 0.1))

    def __draw_tower_parameter(self, parameter_image, number_this_parameter, value, height, context, additional_text =''):  # рисует параметры башни в магазине
        context.get_config_parameter_scene().get_screen().blit(parameter_image, (height * 0.05, height * 0.16 + 170 + number_this_parameter * 120))
        Function.draw_text(str(value) + additional_text, 100, (height * 0.25, height * 0.16 + 220 + number_this_parameter * 120), context)


    def build_tower(self, event, scale_tower, level, maps_controller, context):  # проверяет, нажата ли кнопка продуктов и покупает башню
        mouse_pose = pygame.mouse.get_pos()
        current_tile = context.get_config_gameplay().get_current_tile()
        if current_tile is not None:
            for i in self.products:
                if i.coordinate[0] < mouse_pose[0] < i.coordinate[0] + i.scale and i.coordinate[0] < mouse_pose[0] < i.coordinate[0] + i.scale:
                    maps_controller.get_build_array(level)[current_tile]['is_filled'] = i.buy(event, maps_controller.get_build_array(level)[current_tile]['type'], scale_tower, maps_controller.get_build_array(level)[current_tile]['coordinate'], context)
