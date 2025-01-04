import pygame  # импорт библиотеки pygame



class Button:
    # инициализация класса
    def __init__(self, x, y, image, width, height, action, additional_image = None):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__action = action
        self.__image = pygame.image.load(image)
        self.__image = pygame.transform.scale(self.__image, (self.__width, self.__height))
        self.__highlight = pygame.transform.scale(pygame.image.load('images/UI/highlighting/highlightingTower.png'), (self.__width, self.__height))
        if additional_image is not None:
            self.__additional_image = pygame.transform.scale(pygame.image.load(additional_image), (self.__width, self.__height))
        else:
            self.__additional_image = None

    def draw(self, screen):  # функция, рисующая кнопку
        screen.blit(self.__image, (self.__x, self.__y))
        mouse_position = pygame.mouse.get_pos()
        if self.__x + self.__width >= mouse_position[0] >= self.__x and self.__y + self.__height >= mouse_position[1] >= self.__y:
            screen.blit(self.__highlight, (self.__x, self.__y))
        if self.__additional_image is not None:
            screen.blit(self.__additional_image, (self.__x, self.__y))

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


    def change_image(self, new_image):
        self.__image = pygame.transform.scale(pygame.image.load(new_image), (self.__width, self.__height))

