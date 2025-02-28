import pygame

def button_works(event, context):
    if context.get_config_constant_object().get_button_setting().is_pressed(event):
        context.get_config_constant_object().get_button_setting().handle_event_parameter({'context': context, 'lvl': 'setting'})
    if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
        context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context': context, 'lvl': 'mainMenu'})  # кнопка перехода в главное меню нажат
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not context.get_config_gameplay().get_is_fail():  # если кнопка была нажата
        context.get_animation_controller().start_move()  # переменная isMove нужна, чтобы определять, закончено движение или нет
    if pygame.key.get_pressed()[pygame.K_TAB]:  # была нажата кнопка таб
        context.get_config_gameplay().set_use_additional_parameters(True)
    else:
        context.get_config_gameplay().set_use_additional_parameters(False)

def is_started(context):
    if context.get_config_gameplay().get_is_started():  # если кнопка перехода на 1 уровень нажата, то задает рандомно количество врагов от 1 до 3 на 10 волн
        context.get_maps_controller().update_trajectory_array()
        context.get_maps_controller().create_waves(100, context)  # создает волны
        context.get_config_gameplay().set_current_wave(1 - context.get_config_gameplay().get_current_wave())  # текущая волна
        context.get_enemies_controller().create_enemy(context)  # создает врагов на 1 клетке
        context.get_config_gameplay().set_is_started(False)  # переменная отвечает за то, началась ли игра или нет
        context.get_config_gameplay().set_money(-context.get_config_gameplay().get_money() + 1000)
        for i in range(len(context.get_maps_controller().get_build_array())):  # обнуляет все тайлы
            context.get_maps_controller().get_build_array()[i]['is_filled'] = False