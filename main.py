import pygame
import sys

from scripts.configs import maps_controller_class, config_constant_object_class, animation_controller_class, config_gameplay_class, towers_controller_class, enemies_controller_class, config_modifier_class, \
    config_parameter_screen_class, file_save_controller_class, sound_controller_class, event_controller_class, buttons_groups_controller
from scripts import context_class
from scripts.classes_objects import definition_current_tile

from scripts.main_scripts import level_controller, draw_scene

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

file_save_controller = file_save_controller_class.FileSaveController()
config_parameter_screen = config_parameter_screen_class.ConfigParameterScreen()
maps_controller = maps_controller_class.MapsController(config_parameter_screen.get_width(), config_parameter_screen.get_height())
highlighting = definition_current_tile.Highlighting(maps_controller)
config_constant_object = config_constant_object_class.ConfigConstantObject(config_parameter_screen.get_height(), config_parameter_screen.get_width(), highlighting)
config_gameplay = config_gameplay_class.ConfigGameplay(config_parameter_screen.get_height(), file_save_controller)
config_modifier = config_modifier_class.ConfigModifier(False, False, None, None)

towers_controller = towers_controller_class.TowerController(maps_controller.get_tile_scale())
enemies_controller = enemies_controller_class.EnemiesController()
animation_controller = animation_controller_class.AnimationController(config_parameter_screen)
sound_controller = sound_controller_class.SoundController(file_save_controller)
event_controller = event_controller_class.EventController()
buttons_groups_controller = buttons_groups_controller.ButtonGroupController(config_parameter_screen.get_width(), config_parameter_screen.get_height(), sound_controller, config_gameplay)


context = context_class.Context(config_constant_object, config_gameplay, config_modifier, config_parameter_screen, animation_controller, enemies_controller, towers_controller, maps_controller, file_save_controller, sound_controller, event_controller, buttons_groups_controller)
context.buttons_groups_controller.change_buttons_active(context)
while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            sys.exit()
        level_controller.level_controller(event, highlighting, context)
        context.sound_controller.click_sound(event)
    context.animation_controller.move_enemies(context)
    draw_scene.draw_scene(highlighting, context)
    if context.config_gameplay.get_is_fail():
        context.animation_controller.fail_animation(context)
    context.maps_controller.update_trajectory_array()
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.config_constant_object.get_clock().tick(30)  # ограничивает число кадров в секунду