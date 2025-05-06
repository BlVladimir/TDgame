import pygame
from scripts.main_scripts.resourse_path import resource_path

class Highlighting:
    def __init__(self, maps_controller):
        self.__highlight_tile_image = pygame.transform.scale(pygame.image.load(resource_path("images/UI/highlighting/highlighting_tower.png")), (maps_controller.get_tile_scale(), maps_controller.get_tile_scale()))  # картинка выделения

    def update_scale(self, context):  # обновляет размер выделения(т.к. на разных картах разные размеры тайла)
        self.__highlight_tile_image = pygame.transform.scale(pygame.image.load(resource_path("images/UI/highlighting/highlighting_tower.png")), (context.maps_controller.get_tile_scale(), context.maps_controller.get_tile_scale()))

    def draw_highlighting(self, context):  # функция, рисующая выделение тайлов
        if context.config_parameter_scene.get_scene().isdigit():
            if context.config_gameplay.get_current_tile() is not None:
                context.config_parameter_scene.get_screen().blit(self.__highlight_tile_image, context.maps_controller.get_build_array()[context.config_gameplay.get_current_tile()]['coordinate'])  # выделяет # текущий тайл, на котором находится мышка
            if context.config_gameplay.get_highlight_tile() is not None:
                context.config_parameter_scene.get_screen().blit(self.__highlight_tile_image, context.maps_controller.get_build_array()[context.config_gameplay.get_highlight_tile()]['coordinate'])  # выделяет текущий тайл, на который в последний раз нажимала мышка