import Function


#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl1(context, shop, highlighting):
        context.get_config_map().get_map_array()[0].draw(context)
        highlighting.draw_highlighting(context.get_config_map().get_map_array()[0].build_array, context)
        tower_array = context.get_config_gameplay().get_towers_object_array()
        if tower_array:
            for i in tower_array:  # проходится по массиву объектов башен и рисует их
                i.draw_tower(context)
            for i in tower_array:  # проходит по всему массиву башен, и если индекс башни совпадает с текущим тайлом, то вращает башню
                if i.index == context.get_config_gameplay().get_current_tile():
                    i.draw_radius(context)
                    break
        enemy_array = context.get_config_enemy().get_enemy_array()
        for i in range(len(enemy_array)):  # рисует каждого врага
            enemy_array[i].draw(context)
        shop.draw(context)  # рисует магазин(так называется, потому что в будущем будет возможность его закрывать)
        context.get_config_constant_object().get_button_main_manu().draw(context)
        context.get_config_constant_object().get_button_setting().draw(context)
        context.get_config_parameter_scene().get_screen().blit(shop.money_picture, (420, 20))
        Function.draw_text(context.get_config_gameplay().get_amount_of_money(), 100, context.get_config_gameplay().get_amount_of_money_position(), context)
        context.get_config_constant_object().get_information_table().draw(context.get_config_parameter_scene().get_height(), context.get_config_parameter_scene().get_width(), context)
        

