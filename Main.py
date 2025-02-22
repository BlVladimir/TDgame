import pygame
import sys

import MainManu
import Shop
import DefinitionCurrentTile
import LVL1
import Function
from Configs import AnimationControllerClass, ConfigParameterScreenClass, ConfigConstantObjectClass, ConfigGameplayClass, ConfigModifierClass, MapsControllerClass, TowersControllerClass, EnemiesControllerClass
import ContextClass

from EnemyClass import create_waves

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

def action_scene(parameter_dict):  # функция, меняющая переменную сцены
    parameter_dict['context'].get_config_parameter_scene().new_value_scene(parameter_dict['lvl'])
    parameter_dict['context'].get_maps_controller(). change_level(int(parameter_dict['lvl']))

def action_exit():  # функция, закрывающая окно
    pygame.quit()
    sys.exit()

def change_using_additional_parameter(additionalParameters):
    if additionalParameters:
        additionalParameters = False
    else:
        additionalParameters = True
    return additionalParameters

config_parameter_screen = ConfigParameterScreenClass.ConfigParameterScreen(1500, 1000)
config_constant_object = ConfigConstantObjectClass.ConfigConstantObject(config_parameter_screen.get_height(), config_parameter_screen.get_width(), action_exit, action_scene, change_using_additional_parameter)
config_gameplay = ConfigGameplayClass.ConfigGameplay((600, 70))
config_modifier = ConfigModifierClass.ConfigModifier(False, False, None, None)

maps_controller = MapsControllerClass.MapsController(config_parameter_screen.get_width(), config_parameter_screen.get_height())
towers_controller = TowersControllerClass.TowerController(config_parameter_screen.get_tile_scale())
enemies_controller = EnemiesControllerClass.EnemiesController()
animation_controller = AnimationControllerClass.AnimationController()

context = ContextClass.Context(config_constant_object, config_gameplay, config_modifier, config_parameter_screen, animation_controller, enemies_controller, towers_controller, maps_controller)
shop = Shop.Shop(config_parameter_screen.get_height())
highlighting = DefinitionCurrentTile.Highlighting(config_parameter_screen.get_height())

def definition(event, context):
    mouse_pose = pygame.mouse.get_pos()  # получает позицию мышки
    context.get_config_gameplay().new_value_highlight_tile(None)
    if context.get_config_parameter_scene().get_width() - context.get_config_parameter_scene().get_height() * 0.4 > mouse_pose[0] > context.get_config_parameter_scene().get_height() * 0.4:
        tile_scale = context.get_config_parameter_scene().get_tile_scale()
        build_array = context.get_maps_controller().get_build_array()
        for i in range(len(build_array)):  # Проходит по координатам всех тайлов, и если они совпадут с координатой мышки, то этот тайл сохранится как текущий тайл. Если мышка была нажата, та как действующий тайл
            if build_array[i]['coordinate'][0] <= mouse_pose[0] <= build_array[i]['coordinate'][0] + tile_scale and build_array[i]['coordinate'][1] <= mouse_pose[1] <= build_array[i]['coordinate'][1] + tile_scale:
                context.get_config_gameplay().new_value_highlight_tile(i)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    context.get_config_gameplay().new_value_current_tile(i)
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                context.get_config_gameplay().new_value_current_tile(None)

while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # если кнопка была нажата
            if context.get_config_parameter_scene().get_scene() == '1' and event.key == pygame.K_RETURN:  # эта кнопка Enter
                animation_controller.start_move()  # переменная isMove нужна, чтобы определять, закончено движение или нет
        if pygame.key.get_pressed()[pygame.K_TAB]:  # была нажата кнопка таб
            use_additional_parameters = True
        else:
            use_additional_parameters = False
        match context.get_config_parameter_scene().get_scene():
            case 'mainMenu':
                MainManu.handle_event(event, context)  # переменная, равняющаяся True только если кнопка перехода ан 1 уровень нажата
                if context.get_config_gameplay().get_waves():  # обнуляет массив врагов и их количество на каждой волне в меню
                    context.get_config_gameplay().new_value_waves([])
                    context.get_enemies_controller().clear_enemies_array()
                    towers_controller.clear_towers_arrays()
                if context.get_config_constant_object().get_button_setting().is_pressed(event):
                    context.get_config_constant_object().get_button_setting().handle_event_parameter({'context':context, 'lvl':'setting'})
            case '1':
                if context.get_config_gameplay().get_is_started():  # если кнопка перехода на 1 уровень нажата, то задает рандомно количество врагов от 1 до 3 на 10 волн
                    context.get_maps_controller().update_trajectory_array()
                    create_waves(100, 3, context) #  создает волны
                    context.get_config_gameplay().new_value_current_wave(1 - context.get_config_gameplay().get_current_wave())  # текущая волна 1
                    context.get_enemies_controller().create_enemy(context)  # создает врагов на 1 клетке
                    context.get_config_gameplay().new_value_is_started(False)  # переменная отвечает за то, началась ли игра или нет
                    context.get_config_gameplay().new_value_money(-context.get_config_gameplay().get_money() + 1000)
                    for i in range(len(context.get_maps_controller().get_build_array())):  # обнуляет все тайлы
                        context.get_maps_controller().get_build_array()[i]['is_filled'] = False
                context.get_towers_controller().define_current_tower(context)
                context.get_enemies_controller().define_current_enemy()
                if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
                    if context.get_enemies_controller().get_current_enemy():  # если выделенный враг существует и существует хотя бы одна башня
                        if context.get_towers_controller().get_current_tower() and context.get_towers_controller().get_current_tower().is_in_radius(context):  # если индекс башни равен текущему тайлу и текущий враг в радиусе башни
                            context.get_enemies_controller().get_current_enemy().remove_health(context)  # отнимает у врага здоровье, равное урону башни
                            context.get_towers_controller().get_current_tower().is_used = True  # переменная отвечает за то, что башня была использована
                            context.get_enemies_controller().kill_enemies(context)
                definition(event, context)  # определяет текущий тайл
                if context.get_config_gameplay().get_current_tile() is not None and not context.get_maps_controller().get_build_array()[context.get_config_gameplay().get_current_tile()]['is_filled']:
                    context.get_config_gameplay().new_value_shop_type(1)
                elif context.get_config_gameplay().get_current_tile() is not None and context.get_maps_controller().get_build_array()[context.get_config_gameplay().get_current_tile()]['is_filled']:
                    context.get_config_gameplay().new_value_shop_type(2)
                else:
                    context.get_config_gameplay().new_value_shop_type(0)
                if context.get_config_gameplay().get_shop_type() == 1:
                    shop.build_tower(event,context)  # если мышка нажмет на иконку башни в магазине, то башня построится на текущем тайле
                if context.get_towers_controller().get_current_tower():
                    if context.get_towers_controller().get_current_tower().image_gun is not None:
                        context.get_towers_controller().get_current_tower().rotate_gun()
                        context.get_towers_controller().get_current_tower().draw_radius(context)
                    if context.get_towers_controller().get_current_button_update().is_pressed(event):
                        context.get_towers_controller().get_current_button_update().handle_event_parameter(context)
                context.get_config_gameplay().new_value_amount_of_money('x' + str(context.get_config_gameplay().get_money())) #  рисует количество денег
                if context.get_config_constant_object().get_button_setting().is_pressed(event):
                    context.get_config_constant_object().get_button_setting().handle_event_parameter({'context':context, 'lvl':'setting'})
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})  # кнопка перехода в главное меню нажата
            case '2':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case '3':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case '4':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case '5':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case '6':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case 'setting':
                if context.get_config_constant_object().get_button_additional_parameter().is_pressed(event):
                    context.get_config_gameplay().new_value_always_use_additional_parameters(Function.file_change('alwaysUseAdditionalParameter'))
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
        context.get_config_constant_object().get_button_exit().handle_event(event)
    context.get_animation_controller().move_enemies(context)
    if context.get_config_gameplay().get_is_fail():
        scene = 'mainMenu'
    context.get_config_parameter_scene().get_screen().fill((0, 0, 0))  # закрашивает весь экран, чтобы не было видно предыдущую сцену
    context.get_maps_controller().update_trajectory_array()
    match context.get_config_parameter_scene().get_scene():  # То же, что и switch в других языках программирования. В зависимости от значения scene выполняет определенные действия. В данном случае используется для отрисовки определенных объектов
        case 'mainMenu':
            MainManu.draw_buttons(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '1':
            LVL1.draw_lvl1(context, shop, highlighting, maps_controller, towers_controller, enemies_controller)
        case '2':
            context.get_maps_controller().draw_map(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '3':
            context.get_maps_controller().draw_map(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '4':
            context.get_maps_controller().draw_map(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '5':
            context.get_maps_controller().draw_map(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case '6':
            context.get_maps_controller().draw_map(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'setting':
            context.get_config_constant_object().get_button_additional_parameter().draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
    context.get_config_constant_object().get_button_exit().draw(context)  # вне switch, что бы всегда было видно
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.get_config_constant_object().get_clock().tick(60)  # ограничивает число кадров в секунду
