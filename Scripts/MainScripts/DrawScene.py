from Scripts.MainScripts import MainManu, LVL

def draw_scene(highlighting, shop, context):
    context.get_animation_controller().move_enemies(context)
    context.get_config_parameter_scene().get_screen().fill((0, 0, 0))  # закрашивает весь экран, чтобы не было видно предыдущую сцену
    match context.get_config_parameter_scene().get_scene():
        case 'mainMenu':
            MainManu.draw_buttons(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '1':
            LVL.draw_lvl(context, shop, highlighting)
        case '2':
            LVL.draw_lvl(context, shop, highlighting)
        case '3':
            LVL.draw_lvl(context, shop, highlighting)
        case '4':
            LVL.draw_lvl(context, shop, highlighting)
        case '5':
            LVL.draw_lvl(context, shop, highlighting)
        case '6':
            LVL.draw_lvl(context, shop, highlighting)
        case 'setting':
            context.get_config_constant_object().get_button_additional_parameter().draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
    context.get_config_constant_object().get_button_exit().draw(context)  # вне switch, что бы всегда было видно