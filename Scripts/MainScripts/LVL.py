#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl(context, shop, highlighting):
        context.get_maps_controller().draw_map(context)
        highlighting.draw_highlighting(context.get_maps_controller().get_build_array(), context)
        context.get_towers_controller().draw_towers(context)
        context.get_enemies_controller().draw_enemies(context)
        shop.draw(context.get_towers_controller(), context)  # рисует магазин
        context.get_config_constant_object().get_button_main_manu().draw(context)
        context.get_config_constant_object().get_button_setting().draw(context)
        context.get_config_parameter_scene().get_screen().blit(shop.get_money_picture(), (context.get_config_parameter_scene().get_height() * 0.4, context.get_config_parameter_scene().get_height() * 0.05))
        context.get_config_gameplay().draw_money(context)
        context.get_config_constant_object().get_information_table().draw(context.get_config_parameter_scene().get_height(), context.get_config_parameter_scene().get_width(), context)
        context.get_towers_controller().draw_animation_upgrade(context)
        context.get_config_constant_object().update_sprite(context)

        

