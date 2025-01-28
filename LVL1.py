import pygame
import Map
import Shop
import DefinitionCurrentTile
import Function
from MainManu import height


#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl1(screen, button_main_manu, button_setting, money_picture, enemy_array, current_enemy, highlight_tile_images, highlight_tile, current_tile, amount_of_money, amount_of_money_pos, is_used_additional_parameters, always_use, shop_tipe, information_table):
        Map.lvl1.draw(screen)
        DefinitionCurrentTile.draw_highlighting(highlight_tile_images, highlight_tile, current_tile, Map.lvl1.build_array, screen)
        for i in range(len(Shop.towers_object_array)):  # проходится по массиву объектов башен и рисует их
            Shop.towers_object_array[i].draw_tower(screen, is_used_additional_parameters, always_use)
        for i in range(len(enemy_array)):  # рисует каждого врага
            enemy_array[i].draw(screen, always_use, is_used_additional_parameters)
        for i in range(len(Shop.towers_object_array)):  # проходит по всему массиву башен, и если индекс башни совпадает с текущим тайлом, то вращает башню
            if Shop.towers_object_array[i].index == current_tile:
                Shop.towers_object_array[i].draw_radius(screen)
        Shop.draw(shop_tipe, screen, pygame.image.load('images/UI/money.png'), current_tile)  # рисует магазин(так называется, потому что в будущем будет возможность его закрывать)
        button_main_manu.draw(screen)
        button_setting.draw(screen)
        screen.blit(money_picture, (420, 20))
        Function.draw_text(screen, amount_of_money, 100, amount_of_money_pos)
        information_table.draw(screen, height, enemy_array, current_enemy)
        

