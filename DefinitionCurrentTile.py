import pygame
from MainManu import width, height

def definition(event, build_array, scale_tile, current_tile):
    mouse_pose = pygame.mouse.get_pos()  # получает позицию мышки
    dedicatedTile = None
    if width - height * 0.4 > mouse_pose[0] > height * 0.4:
        for i in range(len(build_array)):  # Проходит по координатам всех тайлов, и если они совпадут с координатой мышки, то этот тайл сохранится как текущий тайл. Если мышка была нажата, та как действующий тайл
            if build_array[i]['coordinate'][0] <= mouse_pose[0] <= build_array[i]['coordinate'][0] + scale_tile and build_array[i]['coordinate'][1] <= mouse_pose[1] <= build_array[i]['coordinate'][1] + scale_tile:
                dedicatedTile = i  # + 1, чтобы если ноль, то ничего не выделяло
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_tile = i
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                current_tile = None
    return current_tile, dedicatedTile

def draw_highlighting(highlighting_tile_image, current_tile, highlighting_tile, build_array, screen):  # функция, рисующая выделение тайлов
    if current_tile is not None:
        screen.blit(highlighting_tile_image, build_array[current_tile]['coordinate'])  # выделяет # текущий тайл, на котором находится мышка
    if highlighting_tile is not None:
        screen.blit(highlighting_tile_image, build_array[highlighting_tile]['coordinate'])  # выделяет текущий тайл, на который в последний раз нажимала мышка

def highlight_enemy(enemy_mas):  # определяет врага, на которого наведена мышка
    current_enemy = None
    if enemy_mas:
        scale = enemy_mas[0].scale
        mousePose = pygame.mouse.get_pos()
        for i in range(len(enemy_mas)):
            if enemy_mas[i].rect[0] + scale * 0.9 >= mousePose[0] >= enemy_mas[i].rect[0] + scale * 0.1 and enemy_mas[i].rect[1]  + scale * 0.9 >= mousePose[1] >= enemy_mas[i].rect[1]+ scale * 0.1:
                current_enemy = i
                break
    return current_enemy



