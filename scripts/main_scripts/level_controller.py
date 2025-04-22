from scripts.main_scripts import level, main_menu

def level_controller(shop, event, highlighting, context):  # все действия в игре каждый кадр
    match context.get_config_parameter_scene().get_scene():
        case 'mainMenu':
            main_menu.handle_event(event, context)
            if context.get_config_gameplay().get_waves():  # обнуляет массив врагов и их количество на каждой волне в меню
                context.get_config_gameplay().set_waves([])
                context.get_enemies_controller().clear_enemies_array()
                context.get_towers_controller().clear_towers_arrays()
            if context.get_config_constant_object().get_button_setting().is_pressed(event):
                context.get_config_constant_object().get_button_setting().handle_event_parameter({'context': context, 'lvl': 'setting'})
        case '1':
            level.level(shop, event, highlighting, context)
        case '2':
            level.level(shop, event, highlighting, context)
        case '3':
            level.level(shop, event, highlighting, context)
        case '4':
            level.level(shop, event, highlighting, context)
        case '5':
            level.level(shop, event, highlighting, context)
        case '6':
            level.level(shop, event, highlighting, context)
        case 'setting':
            context.get_settings_objects().action_settings(event, context)
            if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context': context, 'lvl': 'mainMenu'})