import pygame
import sys

from Scripts.Configs import MapsControllerClass, ConfigConstantObjectClass, AnimationControllerClass, ConfigGameplayClass, TowersControllerClass, EnemiesControllerClass, ConfigModifierClass, \
    ConfigParameterScreenClass, FileSaveControllerClass, SoundControllerClass, SettingsObjectsClass
from Scripts import ContextClass
from Scripts.ClassesObjects import ShopClass, DefinitionCurrentTile

from Scripts.MainScripts import LevelController, DrawScene

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

def __action_scene(parameter_dict):  # функция, меняющая переменную сцены
    parameter_dict['context'].get_config_parameter_scene().set_scene(parameter_dict['lvl'])
    if parameter_dict['lvl'].isdigit():
        parameter_dict['context'].get_maps_controller().change_level(parameter_dict['lvl'])

def __action_exit():  # функция, закрывающая окно
    pygame.quit()
    sys.exit()

def __change_using_additional_parameter(additionalParameters):
    if additionalParameters:
        additionalParameters = False
    else:
        additionalParameters = True
    return additionalParameters

file_save_controller = FileSaveControllerClass.FileSaveController()
config_parameter_screen = ConfigParameterScreenClass.ConfigParameterScreen()
config_constant_object = ConfigConstantObjectClass.ConfigConstantObject(config_parameter_screen.get_height(), config_parameter_screen.get_width(), __action_exit, __action_scene)
config_gameplay = ConfigGameplayClass.ConfigGameplay(config_parameter_screen.get_height(), file_save_controller)
config_modifier = ConfigModifierClass.ConfigModifier(False, False, None, None)

maps_controller = MapsControllerClass.MapsController(config_parameter_screen.get_width(), config_parameter_screen.get_height())
towers_controller = TowersControllerClass.TowerController(maps_controller.get_tile_scale())
enemies_controller = EnemiesControllerClass.EnemiesController()
animation_controller = AnimationControllerClass.AnimationController(config_parameter_screen)
sound_controller = SoundControllerClass.SoundController(file_save_controller)
settings_objects = SettingsObjectsClass.SettingsObjects(config_parameter_screen.get_width(), config_parameter_screen.get_height(), __change_using_additional_parameter, sound_controller)

context = ContextClass.Context(config_constant_object, config_gameplay, config_modifier, config_parameter_screen, animation_controller, enemies_controller, towers_controller, maps_controller, file_save_controller, sound_controller, settings_objects)
shop = ShopClass.Shop(config_parameter_screen.get_height())
highlighting = DefinitionCurrentTile.Highlighting(context)
while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            pygame.quit()
            sys.exit()
        context.get_config_constant_object().get_button_exit().handle_event(event)
        LevelController.level_controller(shop, event, highlighting, context)
        context.get_sound_controller().click_sound(event)
    context.get_animation_controller().move_enemies(context)
    DrawScene.draw_scene(highlighting, shop, context)
    if context.get_config_gameplay().get_is_fail():
        context.get_animation_controller().fail_animation(context)
    context.get_maps_controller().update_trajectory_array()
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.get_config_constant_object().get_clock().tick(30)  # ограничивает число кадров в секунду