from random import randrange

import pygame
import random


pygame.font.init()


def draw_text(screen, words, size, coordinate_center): #  рисует текст
    f = pygame.font.Font(None, size)
    text = f.render(words, False, (255, 255, 255))
    rect_text = text.get_rect(center = coordinate_center)

    screen.blit(text, rect_text)

def bugs(context): #  модификаторы при убийстве врагов
    type_of_bugs = randrange(1, 5)
    current_influence = random.getrandbits(1)
    match type_of_bugs:
        case 1:
            if current_influence == 0:
                for i in range(len(context.get_config_shop().get_towers_object_array())):
                    if context.get_config_shop().get_towers_object_array()[i].damage > 1:
                        context.get_config_shop().get_towers_object_array()[i].damage -= 1
            else:
                for i in range(len(context.get_config_shop().get_towers_object_array())):
                    context.get_config_shop().get_towers_object_array()[i].damage += 1
        case 2:
            enemy_array = context.get_config_gameplay().get_enemy_array()
            if current_influence == 1:
                for i in range(len(enemy_array)):
                    if enemy_array[i].health > 1:
                        enemy_array[i].health -= 1
            else:
                for i in range(len(enemy_array)):
                    enemy_array[i].health += 1
            context.get_config_gameplay().new_value_enemy_array(enemy_array)
        case 3:
            if current_influence == 0:
                if context.get_config_gameplay().get_money() > 0:
                    context.get_config_gameplay().new_value_money(-1)
            else:
                context.get_config_gameplay().new_value_money(1)
        case 4:
            if current_influence == 1:
                context.get_config_modifier().get_new_value_is_free(True)
            else:
                context.get_config_modifier().get_new_value_price_up(True)
    context.get_config_modifier().get_new_value_type_new_modifier(type_of_bugs)
    context.get_config_modifier().get_new_value_influence(current_influence)

def file_change(changed_parameter):  # изменяет значение в файле
    file_save = open('Save', 'r')
    parameter = file_save.readlines()
    file_save.close()
    changed_line = None
    for i in range(len(parameter)):
        if parameter[i].find(changed_parameter) != -1:
            if parameter[i].find('True') != -1:
                new_value = parameter[i].replace('True', 'False')
                changed_line = i
                returning_value = False
            else:
                new_value = parameter[i].replace('False', 'True')
                changed_line = i
                returning_value = True
    file_save = open('Save', 'w')
    for i in range(len(parameter)):
        if i == changed_line:
            file_save.write(new_value)
        else:
            file_save.write(parameter[i])
    file_save.close()
    return returning_value

def find_in_file(changed_parameter):  # находит значение в файле
    file_save = open('Save', 'r')
    parameter = file_save.readlines()
    for i in range(len(parameter)):
        if parameter[i].find(changed_parameter) != -1:
            if parameter[i].find('True') != -1:
                return True
            else:
                return False

def define_current_tower(context):  # определяет текущую башню по индексу
    tower_array = context.get_config_shop().get_towers_object_array()
    if tower_array:
        for i in range(len(tower_array)):
            if tower_array[i].index == context.get_config_gameplay().get_current_tile():
                context.get_config_gameplay().new_value_current_tower(i)
                break



