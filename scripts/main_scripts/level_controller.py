from scripts.main_scripts import level
from pygame import MOUSEBUTTONDOWN

def level_controller(event, highlighting, context):
    if event.type == MOUSEBUTTONDOWN:
        context.event_controller.update(event, context, highlighting)
    match context.config_parameter_scene.get_scene():
        case 'mainMenu':
            if context.config_gameplay.get_waves():  # обнуляет массив врагов и их количество на каждой волне в меню
                context.config_gameplay.set_waves([])
                context.enemies_controller.clear_enemies_array()
                context.towers_controller.clear_towers_arrays()
        case '1' | '2' | '3' | '4' | '5' | '6':
            level.level(event, context)