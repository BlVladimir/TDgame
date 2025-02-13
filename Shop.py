import pygame
import Function

pygame.init()



def draw(moneyPicture, context): #  рисует магазин
    if context.get_config_gameplay().get_shop_type() == 1:
        draw_store(moneyPicture, context)
        for i in context.get_config_shop().get_products():
            i.draw(context)
    elif context.get_config_gameplay().get_shop_type() == 2:
        draw_up(context)


def draw_up(context):  # рисует кнопку улучшения
    height = context.get_config_parameter_scene().get_height()
    towers_object_array = context.get_config_shop().get_towers_object_array()
    context.get_config_parameter_scene().get_screen().blit(context.get_config_shop().get_imageShop(), (0, 0))
    Function.define_current_tower(context)
    current_tower = context.get_config_gameplay().get_current_tower()
    if current_tower is not None:
        damage_count = towers_object_array[current_tower].damage
        radius_value = round((towers_object_array[current_tower].radius - 50) / 120, 2)
        towers_object_array[current_tower].draw_picture_tower(height * 0.16, (height * 0.2, 200), context)
        draw_tower_parameter(context.get_config_shop().get_tower_characteristic_image()[0], 0, damage_count, height, context)
        draw_tower_parameter(context.get_config_shop().get_tower_characteristic_image()[1], 1, radius_value, height, context,' tile')
        context.get_config_shop().get_button_update_array()[current_tower].draw(context)

def draw_store(moneyPicture, context): #  проходится по массиву возможных покупок и рисует магазин
    context.get_config_parameter_scene().get_screen().blit(context.get_config_shop().get_imageShop(), (0, 0))
    scale_products = context.get_config_shop().get_scale_products()
    for i in context.get_config_shop().get_products():
        Function.draw_text('x' + str(i.cost), 100, (i.coordinate[0] + scale_products * 1.5, i.coordinate[1] + scale_products * 0.5), context)
        context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(moneyPicture, (scale_products * 0.9, scale_products * 0.9)), (i.coordinate[0] + scale_products * 2.1, i.coordinate[1] + scale_products * 0.1))

def draw_tower_parameter(parameter_image, number_this_parameter, value, height, context, additional_text = ''):  # рисует параметры башни в магазине
    context.get_config_parameter_scene().get_screen().blit(parameter_image, (height * 0.05, height * 0.16 + 170 + number_this_parameter * 120))
    Function.draw_text(str(value) + additional_text, 100, (height * 0.25, height * 0.16 + 220 + number_this_parameter * 120), context)


def build_tower(event, scale_tower, build_array, context):  # проверяет, нажата ли кнопка продуктов и покупает башню
    mouse_pose = pygame.mouse.get_pos()
    current_tile = context.get_config_gameplay().get_current_tile()
    if current_tile is not None:
        for i in context.get_config_shop().get_products():
            if i.coordinate[0] < mouse_pose[0] < i.coordinate[0] + i.scale and i.coordinate[0] < mouse_pose[0] < i.coordinate[0] + i.scale:
                build_array = i.buy(event, build_array[current_tile]['type'], scale_tower, build_array[current_tile]['coordinate'], current_tile, build_array, current_tile, context)
    return build_array #  меняет значение денег
