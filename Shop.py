import pygame
import Function


from ProductClass import Product
pygame.init()


towers_object_array = []
button_update_array = []
isOpen = False
imageShop = pygame.image.load("images/UI/shopBackground.png")
tower_characteristic_image = (pygame.transform.scale(pygame.image.load('images/UI/up/damageUpUp.png'), (100, 100)),
                              pygame.transform.scale(pygame.image.load('images/UI/up/radiusUpUp.png'), (100, 100)))
imageShop = pygame.transform.scale(imageShop, (1000 * 0.4, 1000))
scale_products = 100
products = [Product("images/tower/commonFoundation.png", 3, scale_products, (20, 150),  2, 170, (4, 6), False, 0, "images/tower/commonGun.png"),  # coordinate = (20, 150 + i * 120)
            Product("images/tower/sniperFoundation.png", 5, scale_products, (20, 270),  4, 230, (6, 8), False, 0, "images/tower/sniperGun.png"),
            Product("images/tower/antyShield.png", 4, scale_products, (20, 390),  3, 200, (5, 7), True, 0),
            Product("images/tower/venomFoundation.png", 5, scale_products, (20, 510),  2, 170, (6, 8), False, 2, "images/tower/venomGun.png")]


def draw(state, screen, moneyPicture, context, current_tile = None): #  рисует магазин
    if state == 1:
        draw_store(screen, moneyPicture)
        for i in products:
            i.draw(screen)
    elif state == 2:
        draw_up(screen, current_tile, context)


def draw_up(screen, current_tile, context):  # рисует кнопку улучшения
    config = context.get_config_parameter_scene()
    height = config.get_height()
    screen.blit(imageShop, (0, 0))
    current_tower = Function.define_current_tower(current_tile, towers_object_array)
    if current_tower is not None:
        damage_count = towers_object_array[current_tower].damage
        radius_value = round((towers_object_array[current_tower].radius - 50) / 120, 2)
        towers_object_array[current_tower].draw_picture_tower(screen, height * 0.16, (height * 0.2, 200))
        draw_tower_parameter(screen, tower_characteristic_image[0], 0, damage_count, height)
        draw_tower_parameter(screen, tower_characteristic_image[1], 1, radius_value, height, ' tile')
        button_update_array[current_tower].draw(screen)

def draw_store(screen, moneyPicture): #  проходится по массиву возможных покупок и рисует магазин
    screen.blit(imageShop, (0, 0))
    for i in products:
        Function.draw_text(screen, 'x' + str(i.cost), 100, (i.coordinate[0] + scale_products * 1.5, i.coordinate[1] + scale_products * 0.5))
        screen.blit(pygame.transform.scale(moneyPicture, (scale_products * 0.9, scale_products * 0.9)), (i.coordinate[0] + scale_products * 2.1, i.coordinate[1] + scale_products * 0.1))

def draw_tower_parameter(screen, parameter_image, number_this_parameter, value, height, additional_text = ''):  # рисует параметры башни в магазине
    screen.blit(parameter_image, (height * 0.05, height * 0.16 + 170 + number_this_parameter * 120))
    Function.draw_text(screen, str(value) + additional_text, 100, (height * 0.25, height * 0.16 + 220 + number_this_parameter * 120))


def build_tower(event, coins, scale_tower, current_tile, build_array, is_free, price_up):  # проверяет, нажата ли кнопка продуктов и покупает башню
    mouse_pose = pygame.mouse.get_pos()
    if current_tile is not None:
        for i in products:
            if i.coordinate[0] < mouse_pose[0] < i.coordinate[0] + i.scale and i.coordinate[0] < mouse_pose[0] < i.coordinate[0] + i.scale:
                coins, build_array, is_free, price_up = i.buy(event, towers_object_array, button_update_array, coins, build_array[current_tile]['type'], is_free, price_up, scale_tower, build_array[current_tile]['coordinate'], current_tile, build_array, current_tile)
    return coins, build_array, towers_object_array, button_update_array, is_free, price_up #  меняет значение денег
