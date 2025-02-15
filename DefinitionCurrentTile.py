import pygame

class Highlighting:
    def __init__(self, height):
        self.highlight_tile_image = pygame.transform.scale(pygame.image.load("images/UI/highlighting/highlightingTower.png"), (height * 0.1, height * 0.1))

    def draw_highlighting(self, build_array, context):  # функция, рисующая выделение тайлов
        if context.get_config_gameplay().get_current_tile() is not None:
            context.get_config_parameter_scene().get_screen().blit(self.highlight_tile_image, build_array[context.get_config_gameplay().get_current_tile()]['coordinate'])  # выделяет # текущий тайл, на котором находится мышка
        if context.get_config_gameplay().get_highlight_tile() is not None:
            context.get_config_parameter_scene().get_screen().blit(self.highlight_tile_image, build_array[context.get_config_gameplay().get_highlight_tile()]['coordinate'])  # выделяет текущий тайл, на который в последний раз нажимала мышка




