import pygame  # импорт библиотеки pygame

from scripts.main_scripts.function import draw_text

class Button(pygame.sprite.Sprite):
    # инициализация класса
    def __init__(self, x, y, image, width, height, action, name):
        pygame.sprite.Sprite.__init__(self)
        self.rect = [x, y]
        self.__width = width  # ширина
        self.__height = height  # высота
        self.__action = action  # действие(функция, которая вызывается при нажатии)
        self.image = pygame.transform.scale(pygame.image.load(image), (self.__width, self.__height))
        self.__highlight = pygame.transform.scale(pygame.image.load('images/UI/highlighting/highlighting_tower.png'), (self.__width, self.__height))  # выделение кнопки
        self.__show_sprite = True
        self.__name = name

    def update(self, context):
        mouse_position = pygame.mouse.get_pos()
        if self.rect[0] + self.__width >= mouse_position[0] >= self.rect[0] and self.rect[1] + self.__height >= mouse_position[1] >= self.rect[1]:
            context.config_parameter_scene.get_screen().blit(self.__highlight, self.rect)

    def is_pressed(self, event): # функция, считывающая нажатие кнопки
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect[0] + self.__width >= event.pos[0] >= self.rect[0] and self.rect[1] + self.__height >= event.pos[1] >= self.rect[1]:
            return True
        else:
            return False  # Возвращает правду, если нажата и ложь, если не нажата. Нужно, чтобы сделать действие, следующие сразу после нажатия кнопки

    def handle_event_parameter(self, **kwargs):
        return self.__action(kwargs)  # Функция, выполняющая действие, но с параметром. Нужно, чтобы не писать под открытие каждого уровня свою функцию


    def change_image(self, new_image):  # меняет картинку кнопки
        self.image = pygame.transform.scale(pygame.image.load(new_image), (self.__width, self.__height))

    @property
    def name(self):
        return self.__name

class ButtonWithAdditionalImage(Button):
    def __init__(self, x, y, image, width, height, action, name, additional_image):
        super().__init__(x, y, image, width, height, action, name)
        self.__additional_image = pygame.transform.scale(pygame.image.load(additional_image), (self.__width, self.__height))  # картинка, которая накладывается при отрисовки кнопки

    def update(self, **kwargs):
        kwargs['context'].config_parameter_scene.get_screen().blit(self.__additional_image, self.rect)
        super().update(kwargs['context'])

class ButtonWithText(Button):
    def __init__(self, x, y, image, width, height, action, name):
        super().__init__(x, y, image, width, height, action, name)

    def update(self, **kwargs):
        super().update(kwargs['context'])
        draw_text(kwargs['text'], int(self.__width/len(kwargs['text'])) * 3, (self.rect[0] + self.__width/2, self.rect[1] + self.__height/2), kwargs['context'])