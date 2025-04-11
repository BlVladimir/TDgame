import pygame

class Highlighting:
    def __init__(self, context):
        self.__highlight_tile_image = pygame.transform.scale(pygame.image.load("images/UI/highlighting/highlighting_tower.png"), (context.get_maps_controller().get_tile_scale(), context.get_maps_controller().get_tile_scale()))  # картинка выделения

    def update_scale(self, context):  # обновляет размер выделения(т.к. на разных картах разные размеры тайла)
        self.__highlight_tile_image = pygame.transform.scale(pygame.image.load("images/UI/highlighting/highlighting_tower.png"), (context.get_maps_controller().get_tile_scale(), context.get_maps_controller().get_tile_scale()))

    def draw_highlighting(self, build_array, context):  # функция, рисующая выделение тайлов
        if context.get_config_parameter_scene().get_scene().isdigit():
            if context.get_config_gameplay().get_current_tile() is not None:
                context.get_config_parameter_scene().get_screen().blit(self.__highlight_tile_image, build_array[context.get_config_gameplay().get_current_tile()]['coordinate'])  # выделяет # текущий тайл, на котором находится мышка
            if context.get_config_gameplay().get_highlight_tile() is not None:
                context.get_config_parameter_scene().get_screen().blit(self.__highlight_tile_image, build_array[context.get_config_gameplay().get_highlight_tile()]['coordinate'])  # выделяет текущий тайл, на который в последний раз нажимала мышка