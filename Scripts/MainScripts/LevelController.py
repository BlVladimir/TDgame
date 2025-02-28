from Scripts.MainScripts import Level, Function, MainManu

def level_controller(shop, event, context):
    match context.get_config_parameter_scene().get_scene():
        case 'mainMenu':
            MainManu.handle_event(event, context)
            if context.get_config_gameplay().get_waves():  # обнуляет массив врагов и их количество на каждой волне в меню
                context.get_config_gameplay().set_waves([])
                context.get_enemies_controller().clear_enemies_array()
                context.get_towers_controller().clear_towers_arrays()
            if context.get_config_constant_object().get_button_setting().is_pressed(event):
                context.get_config_constant_object().get_button_setting().handle_event_parameter({'context': context, 'lvl': 'setting'})
        case '1':
            Level.level(shop, event, context)
        case '2':
            Level.level(shop, event, context)
        case '3':
            Level.level(shop, event, context)
        case '4':
            Level.level(shop, event, context)
        case '5':
            Level.level(shop, event, context)
        case '6':
            Level.level(shop, event, context)
        case 'setting':
            if context.get_config_constant_object().get_button_additional_parameter().is_pressed(event):
                context.get_config_gameplay().set_always_use_additional_parameters(Function.file_change('alwaysUseAdditionalParameter'))
            if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context': context, 'lvl': 'mainMenu'})