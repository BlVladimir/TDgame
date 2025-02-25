from Scripts.MainScripts import Function


#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl1(context, shop, highlighting, maps_controller, towers_controller, enemies_controller):
        maps_controller.draw_map(context)
        highlighting.draw_highlighting(maps_controller.get_build_array(), context)
        towers_controller.draw_towers(context)
        enemies_controller.draw_enemies(context)
        shop.draw(towers_controller, context)  # рисует магазин
        context.get_config_constant_object().get_button_main_manu().draw(context)
        context.get_config_constant_object().get_button_setting().draw(context)
        context.get_config_parameter_scene().get_screen().blit(shop.money_picture, (420, 20))
        Function.draw_text(context.get_config_gameplay().get_amount_of_money(), 100, context.get_config_gameplay().get_amount_of_money_position(), context)
        context.get_config_constant_object().get_information_table().draw(context.get_config_parameter_scene().get_height(), context.get_config_parameter_scene().get_width(), enemies_controller, context)
        towers_controller.draw_animation_upgrade(context)
        

