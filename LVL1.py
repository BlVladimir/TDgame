import pygame
import Shop
import DefinitionCurrentTile
import Function


#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl1(screen, button_main_manu, button_setting, money_picture, enemy_array, current_enemy, highlight_tile_images, highlight_tile, current_tile, amount_of_money, amount_of_money_pos, is_used_additional_parameters, always_use, shop_tipe, information_table, context):
        context.get_config_map().get_map_array()[0].draw(screen)
        DefinitionCurrentTile.draw_highlighting(highlight_tile_images, highlight_tile, current_tile, context.get_config_map().get_map_array()[0].build_array, screen)
        tower_array = context.get_config_shop().get_towers_object_array()
        if tower_array:
            for i in tower_array:  # проходится по массиву объектов башен и рисует их
                i.draw_tower(screen, is_used_additional_parameters, always_use)
            for i in tower_array:  # проходит по всему массиву башен, и если индекс башни совпадает с текущим тайлом, то вращает башню
                if i.index == current_tile:
                    i.draw_radius(screen)
                    break
        for i in range(len(enemy_array)):  # рисует каждого врага
            enemy_array[i].draw(screen, always_use, is_used_additional_parameters)
        Shop.draw(shop_tipe, screen, pygame.image.load('images/UI/money.png'), context, current_tile)  # рисует магазин(так называется, потому что в будущем будет возможность его закрывать)
        button_main_manu.draw(screen)
        button_setting.draw(screen)
        screen.blit(money_picture, (420, 20))
        Function.draw_text(screen, amount_of_money, 100, amount_of_money_pos)
        information_table.draw(screen, context.get_config_parameter_scene().get_height(), context.get_config_parameter_scene().get_width(), enemy_array, current_enemy, context)
        

