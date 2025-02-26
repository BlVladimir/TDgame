import pygame
import sys

from Scripts.Configs import MapsControllerClass, ConfigConstantObjectClass, AnimationControllerClass, ConfigGameplayClass, TowersControllerClass, EnemiesControllerClass, ConfigModifierClass, \
    ConfigParameterScreenClass
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

config_parameter_screen = ConfigParameterScreenClass.ConfigParameterScreen(1500, 1000)
config_constant_object = ConfigConstantObjectClass.ConfigConstantObject(config_parameter_screen.get_height(), config_parameter_screen.get_width(), __action_exit, __action_scene, __change_using_additional_parameter)
config_gameplay = ConfigGameplayClass.ConfigGameplay((600, 70))
config_modifier = ConfigModifierClass.ConfigModifier(False, False, None, None)

maps_controller = MapsControllerClass.MapsController(config_parameter_screen.get_width(), config_parameter_screen.get_height())
towers_controller = TowersControllerClass.TowerController(config_parameter_screen.get_tile_scale())
enemies_controller = EnemiesControllerClass.EnemiesController()
animation_controller = AnimationControllerClass.AnimationController(config_parameter_screen)

context = ContextClass.Context(config_constant_object, config_gameplay, config_modifier, config_parameter_screen, animation_controller, enemies_controller, towers_controller, maps_controller)
shop = ShopClass.Shop(config_parameter_screen.get_height())
highlighting = DefinitionCurrentTile.Highlighting(config_parameter_screen.get_height())

while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            pygame.quit()
            sys.exit()
        context.get_config_constant_object().get_button_exit().handle_event(event)
        LevelController.level_controller(shop, event, context)
    context.get_animation_controller().move_enemies(context)
    DrawScene.draw_scene(highlighting, shop, context)
    if context.get_config_gameplay().get_is_fail():
        context.get_animation_controller().fail_animation(context)
    context.get_maps_controller().update_trajectory_array()
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.get_config_constant_object().get_clock().tick(60)  # ограничивает число кадров в секунду