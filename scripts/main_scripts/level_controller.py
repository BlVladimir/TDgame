from scripts.main_scripts import level, main_menu

def level_controller(event, highlighting, context):
    context.event_controller.update(context)
    match context.config_parameter_scene.get_scene():
        case 'mainMenu':
            main_menu.handle_event(event, context)
            if context.config_gameplay.get_waves():  # обнуляет массив врагов и их количество на каждой волне в меню
                context.config_gameplay.set_waves([])
                context.enemies_controller.clear_enemies_array()
                context.towers_controller.clear_towers_arrays()
            if context.config_constant_object.get_button_setting().is_pressed(event):
                context.config_constant_object.get_button_setting().handle_event_parameter({'context': context, 'lvl': 'setting'})
        case '1' | '2' | '3' | '4' | '5' | '6':
            level.level(event, highlighting, context)
        case 'setting':
            context.settings_objects.action_settings(event, context)
            if context.config_constant_object.get_button_main_manu().is_pressed(event):
                context.config_constant_object.get_button_main_manu().handle_event_parameter({'context': context, 'lvl': 'mainMenu'})