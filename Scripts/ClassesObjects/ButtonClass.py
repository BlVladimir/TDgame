import pygame  # импорт библиотеки pygame
from Scripts.MainScripts.Function import draw_text

class Button:
    # инициализация класса
    def __init__(self, x, y, image, width, height, action, additional_image = None):
        self.__x = x  # координата x
        self.__y = y  # координата Y
        self.__width = width  # ширина
        self.__height = height  # высота
        self.__action = action  # действие(функция, которая вызывается при нажатии)
        self.__image = pygame.image.load(image)  # картинка
        self.__image = pygame.transform.scale(self.__image, (self.__width, self.__height))
        self.__highlight = pygame.transform.scale(pygame.image.load('images/UI/highlighting/highlightingTower.png'), (self.__width, self.__height))  # выделение кнопки
        if additional_image is not None:
            self.__additional_image = pygame.transform.scale(pygame.image.load(additional_image), (self.__width, self.__height))  # картинка, которая накладывается при отрисовки кнопки
        else:
            self.__additional_image = None

    def draw(self, context):  # функция, рисующая кнопку
        context.get_config_parameter_scene().get_screen().blit(self.__image, (self.__x, self.__y))
        mouse_position = pygame.mouse.get_pos()
        if self.__x + self.__width >= mouse_position[0] >= self.__x and self.__y + self.__height >= mouse_position[1] >= self.__y:
            context.get_config_parameter_scene().get_screen().blit(self.__highlight, (self.__x, self.__y))
        if self.__additional_image is not None:
            context.get_config_parameter_scene().get_screen().blit(self.__additional_image, (self.__x, self.__y))

    def draw_button_with_text(self, text, context):
        self.draw(context)
        draw_text(text, int(self.__width/len(text)) * 3, (self.__x + self.__width/2, self.__y + self.__height/2), context)

    def is_pressed(self, event): # функция, считывающая нажатие кнопки
        if event.type == pygame.MOUSEBUTTONDOWN and self.__x + self.__width >= event.pos[0] >= self.__x and self.__y + self.__height >= event.pos[1] >= self.__y:
            return True
        else:
            return False  # Возвращает правду, если нажата и ложь, если не нажата. Нужно, чтобы сделать действие, следующие сразу после нажатия кнопки

    def handle_event(self, event):  # функция, выполняющая действие
        if event.type == pygame.MOUSEBUTTONDOWN and self.__x + self.__width >= event.pos[0] >= self.__x and self.__y + self.__height >= event.pos[1] >= self.__y: # мышка находится в координатах кнопки
            self.__action()

    def handle_event_parameter(self, parameter):
        return self.__action(parameter)  # Функция, выполняющая действие, но с параметром. Нужно, чтобы не писать под открытие каждого уровня свою функцию


    def change_image(self, new_image):  # меняет картинку кнопки
        self.__image = pygame.transform.scale(pygame.image.load(new_image), (self.__width, self.__height))

