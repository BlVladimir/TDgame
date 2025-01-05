import pygame

import MainManu
import TowerClass
import ButtonClass
import Function
import ProductClass

from MainManu import  height
pygame.init()

isOpen = False
imageShop = pygame.image.load("images/UI/shopBackground.png")
tower_characteristic_image = (pygame.transform.scale(pygame.image.load('images/UI/up/damageUpUp.png'), (100, 100)),
                              pygame.transform.scale(pygame.image.load('images/UI/up/radiusUpUp.png'), (100, 100)))
imageShop = pygame.transform.scale(imageShop, (height * 0.4, height))
towers_object_array = []
button_update_array = []
# button_buy_array = []
# products_image_file = [["images/tower/commonFoundation.png", "images/tower/commonGun.png"],
#                        ["images/tower/sniperFoundation.png", "images/tower/sniperGun.png"]]
# cost_mas = [3, 5]
scale_products = 100
products = [ProductClass.Product("images/tower/commonFoundation.png", 3, scale_products, (20, 150),  2, 170, (4, 6), "images/tower/commonGun.png"),  # coordinate = (20, 150 + i * 120)
            ProductClass.Product("images/tower/sniperFoundation.png", 5, scale_products, (20, 270),  3, 230, (6, 8), "images/tower/sniperGun.png")]


# position_products = [] #  создание массива координат продуктов
# for i in range(len(products)):
#     position_products.append((20, 150 + i * 120))


def draw(state, screen, moneyPicture, current_tile = None): #  в будущим магазин будет закрываться
    if state == 1:
        for i in products:
            i.draw(screen)
    elif state == 2:
        draw_up(screen, current_tile)

# def draw_store(screen, moneyPicture): #  проходится по массиву возможных покупок и рисует магазин
#     screen.blit(imageShop, (0, 0))
#     if MainManu.scene == "lvl1":
#         for p in range(len(products)):
#             for q in range(len(products[p]) - 1):
#                 screen.blit(products[p][q], position_products[p])
#                 Function.draw_text(screen, 'x' + str(cost_mas[p]), 100, (position_products[p][0] + scale_products * 1.5, position_products[p][1] + scale_products * 0.5))
#                 screen.blit(pygame.transform.scale(moneyPicture, (scale_products * 0.9, scale_products * 0.9)), (position_products[p][0] + scale_products * 2.1, position_products[p][1] + scale_products * 0.1))

def draw_up(screen, current_tile):
    screen.blit(imageShop, (0, 0))
    current_tower = Function.define_current_tower(current_tile, towers_object_array)
    if current_tower is not None:
        damage_count = towers_object_array[current_tower].damage
        radius_value = round((towers_object_array[current_tower].radius - 50) / 120, 2)
        towers_object_array[current_tower].draw_picture_tower(screen, height * 0.16, (height * 0.2, 200))
        draw_tower_parameter(screen, tower_characteristic_image[0], 0, damage_count)
        draw_tower_parameter(screen, tower_characteristic_image[1], 1, radius_value, ' tile')
        button_update_array[current_tower].draw(screen)

def draw_tower_parameter(screen, parameter_image, number_this_parameter, value, additional_text = ''):
    screen.blit(parameter_image, (height * 0.05, height * 0.16 + 170 + number_this_parameter * 120))
    Function.draw_text(screen, str(value) + additional_text, 100, (height * 0.25, height * 0.16 + 220 + number_this_parameter * 120))

def upgrade_tower(parameter_array):
    if towers_object_array[parameter_array[0]].level != 3:
        cost = towers_object_array[parameter_array[0]].improve_cost_array[towers_object_array[parameter_array[0]].level - 1]
        if parameter_array[1] >= cost:
            towers_object_array[parameter_array[0]].upgrade(1, 60)
            towers_object_array[parameter_array[0]].level += 1
            button_update_array[parameter_array[0]].change_image('images/upgrade/2lvl.png') if towers_object_array[parameter_array[0]].level == 2 else button_update_array[parameter_array[0]].change_image('images/upgrade/3lvl.png')
            parameter_array[1] -= cost
    return parameter_array[1]


# def can_buy_tower(event, scale):  # если позиция мышки совпадает с кнопкой покупки, то возвращает правду
#     mousePose = pygame.mouse.get_pos()
#     if event.type == pygame.MOUSEBUTTONDOWN and position_products[0][0] <= mousePose[0] <= position_products[0][0] + scale:
#         for p in range (len(position_products)):
#             if position_products[p][1] <= mousePose[1] <= position_products[p][1] + scale:
#                 return p #  возвращает 0, если башня не была куплина или число соответствующая купленной башни

def build_tower(event, coins, scale, current_tile, build_array):
    # type_tower = can_buy_tower(event, scale)
    # if type_tower is not None: #  при переходе в настройки функция выше возвращает пустоту, не понял почему, поэтому просто делаю дополнительную проверку
    #     if coins >= cost_mas[type_tower] and not build_array[current_tile]['is_filled']:  # проверяет, свободен ли текущий тайл, и если кнопка покупки нажата, добавляет в массив объектов башни новую башню
    #         build_array[current_tile]['is_filled'] = True  # клетка занята
    #         add_damage = 0
    #         add_radius = 1 #  дополнительные параметры и множители
    #         match build_array[current_tile]['type']:
    #             case 2:
    #                 add_damage = 1
    #             case 3:
    #                 add_radius = 1.2
    #         match type_tower:
    #             case 0:
    #                 towers_object_array.append(TowerClass.Tower(products_image_file[0][0], 100, 2 + add_damage, build_array[current_tile]['coordinate'], current_tile,(4, 6), products_image_file[0][1], 170 * add_radius))
    #                 button_update_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
    #             case 1:
    #                 towers_object_array.append(TowerClass.Tower(products_image_file[1][0], 100, 3 + add_damage, build_array[current_tile]['coordinate'], current_tile,(6, 8), products_image_file[1][1], 230 * add_radius)) # Добавляет в массив объектов новые объекты
    #                 button_update_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
    #         coins -= cost_mas[type_tower]
    return coins #  меняет значение денег

# for i in range(len(products_image_file)):
#     products.append([])
#     products[i].append(pygame.transform.scale(pygame.image.load(products_image_file[i][0]), (scale_products, scale_products)))
#     if len(products_image_file) == 2:
#         products[i].append(pygame.transform.scale(pygame.image.load(products_image_file[i][1]), (scale_products, scale_products)))
#         button_buy_array.append(ButtonClass.Button(20, 150 + i * 120, products_image_file[i][0], scale_products, scale_products, build_tower, products_image_file[i][1]))
#     else:
#         button_buy_array.append(ButtonClass.Button(20, 150 + i * 120, products_image_file[i][0], scale_products, scale_products, build_tower, products_image_file[i][1]))
#     products[i].append(cost_mas[i]) #  создание массива продуктов


