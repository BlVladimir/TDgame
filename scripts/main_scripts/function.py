from random import randrange

import pygame
import random
pygame.font.init()

def draw_text(words, size, coordinate, context, t = 0): #  рисует текст
    f = pygame.font.Font(None, size)
    text = f.render(words, False, (255, 255, 255))
    if t == 0:
        rect_text = text.get_rect(center = coordinate)
    else:
        rect_text = coordinate
    context.config_parameter_scene.get_screen().blit(text, rect_text)

def bugs(context): #  модификаторы при убийстве врагов
    type_of_bugs = randrange(1, 5)
    current_influence = random.getrandbits(1)
    match type_of_bugs:
        case 1:
            context.towers_controller.change_damage(current_influence)
        case 2:
            context.enemies_controller.change_health_enemy(current_influence)
        case 3:
            if current_influence == 0:
                if context.config_gameplay.get_money()> 0:
                    context.config_gameplay.set_money(-1)
            else:
                context.config_gameplay.set_money(1)
        case 4:
            if current_influence == 1:
                context.config_modifier.get_new_value_is_free(True)
            else:
                context.config_modifier.get_new_value_price_up(True)
    context.config_modifier.get_new_value_type_new_modifier(type_of_bugs)
    context.config_modifier.get_new_value_influence(current_influence)