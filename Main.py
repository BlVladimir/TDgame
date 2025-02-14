import pygame
import sys

import EnemyClass
import MainManu
import Shop
import DefinitionCurrentTile
import LVL1
import Function
from Configs import ConfigParameterScreenClass, ConfigConstantObjectClass, ConfigEnemyClass, ConfigGameplayClass, ConfigMapClass, ConfigModifierClass
import ContextClass

from EnemyClass import create_waves

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

def action_scene(parameter_dict):  # функция, меняющая переменную сцены
    parameter_dict['context'].get_config_parameter_scene().new_value_scene(parameter_dict['lvl'])

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
config_enemy = ConfigEnemyClass.ConfigEnemy()
config_gameplay = ConfigGameplayClass.ConfigGameplay((600, 70))
config_map = ConfigMapClass.ConfigMap(config_parameter_screen.get_width(), config_parameter_screen.get_height())
config_modifier = ConfigModifierClass.ConfigModifier(False, False, None, None)
context = ContextClass.Context(config_constant_object, config_enemy, config_gameplay, config_map, config_modifier, config_parameter_screen)

shop = Shop.Shop(config_parameter_screen.get_height())
highlighting = DefinitionCurrentTile.Highlighting(config_parameter_screen.get_height())

while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # если кнопка была нажата
            if context.get_config_parameter_scene().get_scene() == 'lvl1' and event.key == pygame.K_RETURN:  # эта кнопка Enter
                context.get_config_enemy().new_value_is_move(True)  # переменная isMove нужна, чтобы определять, закончено движение или нет
        if pygame.key.get_pressed()[pygame.K_TAB]:  # была нажата кнопка таб
            use_additional_parameters = True
        else:
            use_additional_parameters = False
        towers_array = context.get_config_gameplay().get_towers_object_array()
        buttons_update_array = context.get_config_gameplay().get_button_update_array()
        match context.get_config_parameter_scene().get_scene():
            case 'mainMenu':
                MainManu.handle_event(event, context)  # переменная, равняющаяся True только если кнопка перехода ан 1 уровень нажата
                if context.get_config_gameplay().get_waves() != [] or context.get_config_enemy().get_enemy_array() != []:  # обнуляет массив врагов и их количество на каждой волне в меню
                    context.get_config_gameplay().new_value_waves([])
                    context.get_config_enemy().new_value_enemy_array([])
                    context.get_config_gameplay().new_value_towers_object_array([])
                    context.get_config_gameplay().new_value_button_update_array([])
                if context.get_config_constant_object().get_button_setting().is_pressed(event):
                    context.get_config_constant_object().get_button_setting().handle_event_parameter({'context':context, 'lvl':'setting'})
            case 'lvl1':
                if context.get_config_gameplay().get_is_started():  # если кнопка перехода на 1 уровень нажата, то задает рандомно количество врагов от 1 до 3 на 10 волн
                    create_waves(100, 3, context) #  создает волны
                    context.get_config_gameplay().new_value_current_wave(1 - context.get_config_gameplay().get_current_wave())  # текущая волна 1
                    EnemyClass.create_enemy_on_lvl1(context)  # создает врагов на 1 клетке
                    context.get_config_gameplay().new_value_is_started(False)  # переменная отвечает за то, началась ли игра или нет
                    context.get_config_gameplay().new_value_money(-context.get_config_gameplay().get_money() + 1000)
                    for i in range(len(config_map.get_map_array()[0].build_array)):  # обнуляет все тайлы
                        config_map.get_map_array()[0].build_array[i]['is_filled'] = False
                if towers_array:
                    Function.define_current_tower(context)
                if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
                    enemy_array = context.get_config_enemy().get_enemy_array()
                    highlighting.highlight_enemy(context)  # определяет, какой враг выделен
                    if context.get_config_enemy().get_current_enemy() is not None and towers_array:  # если выделенный враг существует и существует хотя бы одна башня
                        for i in range(len(towers_array)):  # проходится по всему массиву башен
                            if towers_array[i].index == context.get_config_gameplay().get_current_tile() and towers_array[i].is_in_radius(enemy_array[context.get_config_enemy().get_current_enemy()].get_center()):  # если индекс башни равен текущему тайлу и текущий враг в радиусе башни
                                enemy_array[context.get_config_enemy().get_current_enemy()].remove_health(towers_array[i].damage, towers_array[i].armor_piercing, towers_array[i].poison)  # отнимает у врага здоровье, равное урону башни
                                towers_array[i].is_used = True  # переменная отвечает за то, что башня была использована
                                if enemy_array[context.get_config_enemy().get_current_enemy()].health <= 0:  # проверяет, упало ли здоровье врага ниже 0
                                    enemy_array.pop(context.get_config_enemy().get_current_enemy())  # если да, то удаляет его и прибавляет деньги
                                    context.get_config_enemy().new_value_current_enemy(None)
                                    Function.bugs(context)
                                    context.get_config_gameplay().new_value_money(2)
                                break  # такая башня только одна, поэтому если такое случилось, то прерывает цикл
                                context.get_config_enemy().new_value_enemy_array(enemy_array)
                highlighting.definition(event, config_map.get_map_array()[0].build_array, context)  # определяет текущий тайл
                if context.get_config_gameplay().get_current_tile() is not None and not config_map.get_map_array()[0].build_array[context.get_config_gameplay().get_current_tile()]['is_filled']:
                    context.get_config_gameplay().new_value_shop_type(1)
                elif context.get_config_gameplay().get_current_tile() is not None and config_map.get_map_array()[0].build_array[context.get_config_gameplay().get_current_tile()]['is_filled']:
                    context.get_config_gameplay().new_value_shop_type(2)
                else:
                    context.get_config_gameplay().new_value_shop_type(0)
                if context.get_config_gameplay().get_shop_type() == 1:
                    config_map.get_map_array()[0].build_array = shop.build_tower(event,100, config_map.get_map_array()[0].build_array, context)  # если мышка нажмет на иконку башни в магазине, то башня построится на текущем тайле
                if towers_array:
                    for i in range(len(towers_array)):  # проходит по всему массиву башен, и если индекс башни совпадает с текущим тайлом, то вращает башню
                        if towers_array[i].index == context.get_config_gameplay().get_current_tile() and towers_array[i].image_gun is not None:
                            towers_array[i].rotate_gun()
                            towers_array[i].draw_radius(context)
                if context.get_config_gameplay().get_current_tower() is not None and context.get_config_gameplay().get_button_update_array()[context.get_config_gameplay().get_current_tower()].is_pressed(event):
                    context.get_config_gameplay().get_button_update_array()[context.get_config_gameplay().get_current_tower()].handle_event_parameter(context)
                context.get_config_gameplay().new_value_amount_of_money('x' + str(context.get_config_gameplay().get_money())) #  рисует количество денег
                if context.get_config_constant_object().get_button_setting().is_pressed(event):
                    context.get_config_constant_object().get_button_setting().handle_event_parameter({'context':context, 'lvl':'setting'})
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})  # кнопка перехода в главное меню нажата
            case 'lvl2':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case 'lvl3':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case 'lvl4':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case 'lvl5':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case 'lvl6':
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
            case 'setting':
                if button_additional_parameter.is_pressed(event):
                    context.get_config_gameplay().new_value_always_use_additional_parameters(Function.file_change('alwaysUseAdditionalParameter'))
                if context.get_config_constant_object().get_button_main_manu().is_pressed(event):
                    context.get_config_constant_object().get_button_main_manu().handle_event_parameter({'context':context, 'lvl':'mainMenu'})
        context.get_config_constant_object().get_button_exit().handle_event(event)
    if context.get_config_enemy().get_is_move():  # если движение не законченно, то враг двигается и идет проверка, закончено движение или нет
        is_fail = EnemyClass.move_all_enemies(config_map.get_map_array()[0].gaps, config_map.get_map_array()[0].tile_scale, context)
        if is_fail:
            scene = 'mainMenu'
        context.get_config_enemy().new_value_time(1)
        towers_array = context.get_config_gameplay().get_towers_object_array()
        for i in range(len(towers_array)):
            towers_array[i].is_used = True
        context.get_config_gameplay().new_value_towers_object_array(towers_array)
        if context.get_config_enemy().get_time() % 60 == 0:
            context.get_config_enemy().new_value_time(-context.get_config_enemy().get_time())
            context.get_config_enemy().new_value_is_move(False)
            remove_array = []
            enemy_array = context.get_config_enemy().get_enemy_array()
            for i in range(len(enemy_array)):
                enemy_array[i].treat()
                if enemy_array[i].health <= 0:  # проверяет, упало ли здоровье врага ниже 0
                    remove_array.append(i)
            for i in range(len(remove_array)):
                enemy_array.pop(i)  # если да, то удаляет его и прибавляет деньги
                context.get_config_enemy().new_value_current_enemy(None)
                Function.bugs(context)
                context.get_config_gameplay().new_value_money(2)
            context.get_config_enemy().new_value_enemy_array(enemy_array)

            for i in range(len(context.get_config_gameplay().get_config_gameplay.get_towers_object_array())):
                context.get_config_gameplay().get_config_gameplay.get_towers_object_array()[i].is_used = False  # После окончания движения врагов разрешает пользоваться башнями. Можно добавить модификатор нескольких использований башен или при максимальном уровне
            if context.get_config_gameplay().get_current_wave() != len(context.get_config_gameplay().get_waves()) and context.get_config_gameplay().get_waves() != []:  # после окончания движения создает врага на освободившейся клетке, если количество волн не дошло до конечной волны
                EnemyClass.create_enemy_on_lvl1(context)
                context.get_config_gameplay().new_value_current_wave(1)
    context.get_config_parameter_scene().get_screen().fill((0, 0, 0))  # закрашивает весь экран, чтобы не было видно предыдущую сцену
    context.get_config_map().get_map_array()[0].get_trajectory_array(context)
    match context.get_config_parameter_scene().get_scene():  # То же, что и switch в других языках программирования. В зависимости от значения scene выполняет определенные действия. В данном случае используется для отрисовки определенных объектов
        case 'mainMenu':
            MainManu.draw_buttons(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'lvl1':
            LVL1.draw_lvl1(context, shop, highlighting)
        case 'lvl2':
            config_map.get_map_array()[1].draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'lvl3':
            config_map.get_map_array()[2].draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'lvl4':
            config_map.get_map_array()[3].draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'lvl5':
            config_map.get_map_array()[4].draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'lvl6':
            config_map.get_map_array()[5].draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
            context.get_config_constant_object().get_button_setting().draw(context)
        case 'setting':
            context.get_config_constant_object().get_button_additional_parameter().draw(context)
            context.get_config_constant_object().get_button_main_manu().draw(context)
    context.get_config_constant_object().get_button_exit().draw(context)  # вне switch, что бы всегда было видно
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.get_config_constant_object().get_clock().tick(60)  # ограничивает число кадров в секунду
