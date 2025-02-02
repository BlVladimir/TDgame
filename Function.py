from random import randrange

import pygame
import random


pygame.font.init()

is_free = False
price_up = False
type_new_modifier = None
influence = None

def draw_text(screen, words, size, coordinate_center): #  рисует текст
    f = pygame.font.Font(None, size)
    text = f.render(words, False, (255, 255, 255))
    rect_text = text.get_rect(center = coordinate_center)

    screen.blit(text, rect_text)

def bugs(tower_array, enemy_array, money, current_is_free, current_price_up): #  модификаторы при убийстве врагов
    type_of_bugs = randrange(1, 5)
    influence = random.getrandbits(1)
    is_free_new = current_is_free
    price_up_new = current_price_up
    match type_of_bugs:
        case 1:
            if influence == 0:
                for i in range(len(tower_array)):
                    if tower_array[i].damage > 1:
                        tower_array[i].damage -= 1
                print('damage - 1')
            else:
                for i in range(len(tower_array)):
                    tower_array[i].damage += 1
                print('damage + 1')
        case 2:
            if influence == 1:
                for i in range(len(enemy_array)):
                    if enemy_array[i].health > 1:
                        enemy_array[i].health -= 1
                print('health - 1')
            else:
                for i in range(len(enemy_array)):
                    enemy_array[i].health += 1
                print('health + 1')
        case 3:
            if influence == 0:
                if money > 0:
                    money -= 1
                print('money - 1')
            else:
                money += 1
                print('money + 1')
        case 4:
            if influence == 1:
                is_free_new = True
                print('free tower')
            else:
                price_up_new = True
                print('price up')
    return money, is_free_new, price_up_new, type_of_bugs, influence

def file_change(changed_parameter):  # изменяет значение в файле
    file_save = open('Save', 'r')
    parameter = file_save.readlines()
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
    file_save.close()
    file_save = open('Save', 'w')
    for i in range(len(parameter)):
        if i == changed_line:
            file_save.write(new_value)
        else:
            file_save.write(parameter[i])
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

def define_current_tower(current_tile, tower_array):  # определяет текущую башню по индексу
    for i in range(len(tower_array)):
        if tower_array[i].index == current_tile:
            return i



