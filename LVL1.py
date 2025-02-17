import Function


#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl1(context, shop, highlighting, maps_controller, level, towers_controller):
        maps_controller.draw_map(level, context)
        highlighting.draw_highlighting(maps_controller.get_build_array(level), context)
        towers_controller.draw_towers(context)
        enemy_array = context.get_config_enemy().get_enemy_array()
        for i in range(len(enemy_array)):  # рисует каждого врага
            enemy_array[i].draw(context)
        shop.draw(towers_controller, context)  # рисует магазин
        context.get_config_constant_object().get_button_main_manu().draw(context)
        context.get_config_constant_object().get_button_setting().draw(context)
        context.get_config_parameter_scene().get_screen().blit(shop.money_picture, (420, 20))
        Function.draw_text(context.get_config_gameplay().get_amount_of_money(), 100, context.get_config_gameplay().get_amount_of_money_position(), context)
        context.get_config_constant_object().get_information_table().draw(context.get_config_parameter_scene().get_height(), context.get_config_parameter_scene().get_width(), context)
        

