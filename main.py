import pygame
import sys

from scripts.configs import config_constant_object_class, animation_controller_class, config_gameplay_class, config_modifier_class, \
    config_parameter_screen_class, file_save_controller_class, sound_controller_class, event_controller_class, buttons_groups_controller
from scripts.iterators import towers_array_iterator, maps_array_iterator, enemies_array_iterator
from scripts import context_class
from scripts.classes_objects import definition_current_tile

from scripts.main_scripts import level_controller, draw_scene

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

file_save_controller = file_save_controller_class.FileSaveController()
config_parameter_screen = config_parameter_screen_class.ConfigParameterScreen()
maps_array_iterator = maps_array_iterator.MapsArrayIterator(config_parameter_screen.get_width(), config_parameter_screen.get_height())
highlighting = definition_current_tile.Highlighting(maps_array_iterator)
config_constant_object = config_constant_object_class.ConfigConstantObject(config_parameter_screen.get_height(), config_parameter_screen.get_width(), highlighting)
config_gameplay = config_gameplay_class.ConfigGameplay(config_parameter_screen.get_height(), file_save_controller)
config_modifier = config_modifier_class.ConfigModifier(False, False, None, None)

towers_array_iterator = towers_array_iterator.TowerArrayIterator(maps_array_iterator.get_tile_scale())
enemies_array_iterator = enemies_array_iterator.EnemiesArrayIterator()
animation_controller = animation_controller_class.AnimationController(config_parameter_screen)
sound_controller = sound_controller_class.SoundController(file_save_controller)
event_controller = event_controller_class.EventController()
buttons_groups_controller = buttons_groups_controller.ButtonGroupController(config_parameter_screen.get_width(), config_parameter_screen.get_height(), sound_controller, config_gameplay)


context = context_class.Context(config_constant_object, config_gameplay, config_modifier, config_parameter_screen, animation_controller, enemies_array_iterator, towers_array_iterator, maps_array_iterator, file_save_controller, sound_controller, event_controller, buttons_groups_controller)
context.buttons_groups_controller.change_buttons_active(context)
while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            sys.exit()
        level_controller.level_controller(event, highlighting, context)
        context.sound_controller.click_sound(event)
        context.maps_array_iterator.definition_current_tile(event, context)
    context.animation_controller.move_enemies(context)
    draw_scene.draw_scene(highlighting, context)
    if context.config_gameplay.get_is_fail():
        context.animation_controller.fail_animation(context, highlighting)
    context.maps_array_iterator.update_trajectory_array()
    pygame.display.flip()  # обновляет экран по завершению цикла
    context.config_constant_object.get_clock().tick(30)  # ограничивает число кадров в секунду