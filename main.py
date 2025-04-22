import pygame
import sys

from scripts.configs import maps_controller_class, config_constant_object_class, animation_controller_class, config_gameplay_class, towers_controller_class, enemies_controller_class, config_modifier_class, \
    config_parameter_screen_class, file_save_controller_class, sound_controller_class, settings_objects_class
from scripts import context_class
from scripts.classes_objects import shop_class, definition_current_tile
from scripts.main_scripts import level_controller, draw_scene

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

def __action_scene(parameter_dict):  # функция, меняющая переменную сцены
    parameter_dict['context'].get_config_parameter_scene().set_scene(parameter_dict['lvl'])
    if parameter_dict['lvl'].isdigit():
        parameter_dict['context'].get_maps_controller().change_level(parameter_dict['lvl'])

def __action_exit():  # функция, закрывающая окно
    pygame.quit()
    sys.exit()

def __change_using_additional_parameter(additionalParameters):  # включает и выключает использование дополнительных параметров
    additionalParameters = not additionalParameters
    return additionalParameters

file_save_controller = file_save_controller_class.FileSaveController()
config_parameter_screen = config_parameter_screen_class.ConfigParameterScreen()
config_constant_object = config_constant_object_class.ConfigConstantObject(config_parameter_screen.get_height(), config_parameter_screen.get_width(), __action_exit, __action_scene)
config_gameplay = config_gameplay_class.ConfigGameplay(config_parameter_screen.get_height(), file_save_controller)
config_modifier = config_modifier_class.ConfigModifier(False, False, None, None)

maps_controller = maps_controller_class.MapsController(config_parameter_screen.get_width(), config_parameter_screen.get_height())
towers_controller = towers_controller_class.TowerController(maps_controller.get_tile_scale())
enemies_controller = enemies_controller_class.EnemiesController()
animation_controller = animation_controller_class.AnimationController(config_parameter_screen)
sound_controller = sound_controller_class.SoundController(file_save_controller)
settings_objects = settings_objects_class.SettingsObjects(config_parameter_screen.get_width(), config_parameter_screen.get_height(), __change_using_additional_parameter, sound_controller)

context = context_class.Context(config_constant_object, config_gameplay, config_modifier, config_parameter_screen, animation_controller, enemies_controller, towers_controller, maps_controller, file_save_controller, sound_controller, settings_objects)
shop = shop_class.Shop(config_parameter_screen.get_height())
highlighting = definition_current_tile.Highlighting(context)
while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            sys.exit()
        context.get_config_constant_object().get_button_exit().handle_event(event)
        level_controller.level_controller(shop, event, highlighting, context)
        context.get_sound_controller().click_sound(event)
    context.get_animation_controller().move_enemies(context)
    draw_scene.draw_scene(highlighting, shop, context)
    if context.get_config_gameplay().get_is_fail():
        context.get_animation_controller().fail_animation(context)
    context.get_maps_controller().update_trajectory_array()
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.get_config_constant_object().get_clock().tick(30)  # ограничивает число кадров в секунду