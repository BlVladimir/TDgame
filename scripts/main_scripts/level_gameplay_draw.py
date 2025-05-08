#  вся отрисовка вынесена в отдельный файл, чтобы не захламлять основной

def draw_lvl(context, highlighting):
        context.maps_array_iterator.draw_map(context)
        highlighting.draw_highlighting(context)
        context.towers_array_iterator.draw_towers(context)
        context.enemies_array_iterator.draw_enemies(context)
        context.config_parameter_scene.get_screen().blit(context.config_constant_object.shop.get_money_picture(), (context.config_parameter_scene.get_height()* 0.4, context.config_parameter_scene.get_height()* 0.05))

        context.config_constant_object.get_information_table().draw(context.config_parameter_scene.get_height(), context.config_parameter_scene.get_width(), context)
        context.towers_array_iterator.draw_animation_upgrade(context)
        context.config_constant_object.shop.draw(context.towers_array_iterator, context)  # рисует магазин
        context.config_gameplay.draw_money(context)