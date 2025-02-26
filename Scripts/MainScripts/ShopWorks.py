def shop_works(shop, event, context):
    if context.get_config_gameplay().get_current_tile() is None:
        context.get_config_gameplay().set_shop_type(0)
    elif context.get_maps_controller().get_build_array()[context.get_config_gameplay().get_current_tile()]['is_filled']:
        context.get_config_gameplay().set_shop_type(2)
    else:
        context.get_config_gameplay().set_shop_type(1)
    if context.get_config_gameplay().get_shop_type() == 1:
        shop.build_tower(event, context)  # если мышка нажмет на иконку башни в магазине, то башня построится на текущем тайле
    if context.get_towers_controller().get_current_tower():
        if context.get_towers_controller().get_current_tower().image_gun is not None:
            context.get_towers_controller().get_current_tower().rotate_gun()
            context.get_towers_controller().get_current_tower().draw_radius(context)
        if context.get_towers_controller().get_current_button_update().is_pressed(event):
            context.get_towers_controller().get_current_button_update().handle_event_parameter(context)
    context.get_config_gameplay().set_amount_of_money('x' + str(context.get_config_gameplay().get_money()))  # рисует количество денег