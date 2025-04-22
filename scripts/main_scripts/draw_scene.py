from scripts.main_scripts import main_menu, level_gameplay_draw

def draw_scene(highlighting, shop, context):  # отрисовка всей игры
    context.get_animation_controller().move_enemies(context)
    context.get_config_parameter_scene().get_screen().fill((0, 0, 0))  # закрашивает весь экран, чтобы не было видно предыдущую сцену
    match context.get_config_parameter_scene().get_scene():
        case 'mainMenu':
            main_menu.draw_buttons(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '1':
            level_gameplay_draw.draw_lvl(context, shop, highlighting)
        case '2':
            level_gameplay_draw.draw_lvl(context, shop, highlighting)
        case '3':
            level_gameplay_draw.draw_lvl(context, shop, highlighting)
        case '4':
            level_gameplay_draw.draw_lvl(context, shop, highlighting)
        case '5':
            level_gameplay_draw.draw_lvl(context, shop, highlighting)
        case '6':
            level_gameplay_draw.draw_lvl(context, shop, highlighting)
        case 'setting':
            context.get_settings_objects().draw_buttons(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
    context.get_config_constant_object().get_button_exit().draw(context)  # вне switch, что бы всегда было видно