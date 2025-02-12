import pygame

def definition(event, build_array, scale_tile, context):
    mouse_pose = pygame.mouse.get_pos()  # получает позицию мышки
    context.get_config_gameplay().new_value_highlight_tile(None)
    if context.get_config_parameter_scene().get_width() - context.get_config_parameter_scene().get_height() * 0.4 > mouse_pose[0] > context.get_config_parameter_scene().get_height() * 0.4:
        for i in range(len(build_array)):  # Проходит по координатам всех тайлов, и если они совпадут с координатой мышки, то этот тайл сохранится как текущий тайл. Если мышка была нажата, та как действующий тайл
            if build_array[i]['coordinate'][0] <= mouse_pose[0] <= build_array[i]['coordinate'][0] + scale_tile and build_array[i]['coordinate'][1] <= mouse_pose[1] <= build_array[i]['coordinate'][1] + scale_tile:
                context.get_config_gameplay().new_value_highlight_tile(i)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    context.get_config_gameplay().new_value_current_tile(i)
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                context.get_config_gameplay().new_value_current_tile(None)

def draw_highlighting(highlighting_tile_image, build_array, screen, context):  # функция, рисующая выделение тайлов
    if context.get_config_gameplay().get_current_tile() is not None:
        screen.blit(highlighting_tile_image, build_array[context.get_config_gameplay().get_current_tile()]['coordinate'])  # выделяет # текущий тайл, на котором находится мышка
    if context.get_config_gameplay().get_highlight_tile() is not None:
        screen.blit(highlighting_tile_image, build_array[context.get_config_gameplay().get_highlight_tile()]['coordinate'])  # выделяет текущий тайл, на который в последний раз нажимала мышка

def highlight_enemy(context):  # определяет врага, на которого наведена мышка
    current_enemy = None
    if context.get_config_gameplay().get_enemy_array():
        scale = context.get_config_gameplay().get_enemy_array()[0].scale
        mousePose = pygame.mouse.get_pos()
        enemy_array = context.get_config_gameplay().get_enemy_array()
        for i in range(len(enemy_array)):
            if enemy_array[i].rect[0] + scale * 0.9 >= mousePose[0] >= enemy_array[i].rect[0] + scale * 0.1 and enemy_array[i].rect[1]  + scale * 0.9 >= mousePose[1] >= enemy_array[i].rect[1]+ scale * 0.1:
                current_enemy = i
                break
    context.get_config_gameplay().new_value_current_enemy(current_enemy)



