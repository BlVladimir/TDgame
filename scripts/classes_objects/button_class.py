import pygame  # импорт библиотеки pygame

from scripts.main_scripts.function import draw_text

class Button(pygame.sprite.Sprite):
    # инициализация класса
    def __init__(self, x, y, image, width, height, event):
        pygame.sprite.Sprite.__init__(self)
        self.rect = [x, y]
        self.__width = width  # ширина
        self.__height = height  # высота
        self.__event = event
        self.image = pygame.transform.scale(pygame.image.load(image), (self.__width, self.__height))
        self.__highlight = pygame.transform.scale(pygame.image.load('images/UI/highlighting/highlighting_tower.png'), (self.__width, self.__height))  # выделение кнопки
        self.__show_sprite = True

    def update(self, context):
        mouse_position = pygame.mouse.get_pos()
        if self.rect[0] + self.__width >= mouse_position[0] >= self.rect[0] and self.rect[1] + self.__height >= mouse_position[1] >= self.rect[1]:
            context.config_parameter_scene.get_screen().blit(self.__highlight, self.rect)

    def is_pressed(self, event): # функция, считывающая нажатие кнопки
        if self.rect[0] + self.__width >= event.pos[0] >= self.rect[0] and self.rect[1] + self.__height >= event.pos[1] >= self.rect[1]:
            return self.__event
        else:
            return False  # Возвращает правду, если нажата и ложь, если не нажата. Нужно, чтобы сделать действие, следующие сразу после нажатия кнопки

class ButtonWithAdditionalImage(Button):
    def __init__(self, x, y, image, width, height, event, additional_image):
        super().__init__(x, y, image, width, height, event)
        self.__additional_image = pygame.transform.scale(pygame.image.load(additional_image), (self.__width, self.__height))  # картинка, которая накладывается при отрисовки кнопки

    def update(self, **kwargs):
        kwargs['context'].config_parameter_scene.get_screen().blit(self.__additional_image, self.rect)
        super().update(kwargs['context'])

class ButtonWithText(Button):
    def __init__(self, x, y, image, width, height, event, text, name):
        super().__init__(x, y, image, width, height, event)
        self.__text = text
        self.__name = name

    def update(self, **kwargs):
        super().update(kwargs['context'])
        draw_text(self.__text, int(self.__width/len(self.__text)) * 3, (self.rect[0] + self.__width/2, self.rect[1] + self.__height/2), kwargs['context'])

    @property
    def text(self):
        raise PermissionError('privet attribute')

    @text.setter
    def text(self, value):
        self.__text = str(value)

    @property
    def name(self):
        return self.__name

class ButtonWithChangeableImage(Button):
    def __init__(self, x, y, image, width, height, action):
        super().__init__(x, y, image, width, height, action)

    def change_image(self, new_image):  # меняет картинку кнопки
        self.image = pygame.transform.scale(pygame.image.load(new_image), (self.__width, self.__height))
'''
class ProductWithoutGun:  # класс продуктов
    def __init__(self, x, y, image, width, height, event, cost, damage, radius, improve_cost_array, armor_piercing, poison):
        self.__button = Button(x, y, image, width, height, event)
        self.__image = image
        self.__cost = cost
        self.__armor_piercing = armor_piercing
        self.__poison = poison
        self.__damage_tower = damage
        self.__radius_tower = radius
        self.__improve_cost_array = improve_cost_array
        self.__additional_money = 0

    def __create_tower(self, price_coefficient, height, context):  # создает башню с характеристиками, зависящими от текущего тайла
        match context.maps_controller.get_build_array()[context.config_gameplay.get_current_tile()]['type']:
            case 1:
                self.__button.is_pressed(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context)
            case 2:
                self.__button.handle_event_parameter(
                    image=self.__image, damage=self.__damage_tower+1, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context)
            case 3:
                self.__button.handle_event_parameter(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower*1.2, height=height, context=context)
            case 4:
                self.__button.handle_event_parameter(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=True,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context)
            case 5:
                self.__button.handle_event_parameter(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison+1, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context)
            case 6:
                self.__button.handle_event_parameter(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money+2, radius=self.__radius_tower, height=height, context=context)
        context.config_gameplay.set_money(-self.__cost * price_coefficient)


    def handle_event_parameter(self, event, **kwargs):  # покупка башни(возможность покупки и покупка, если возможно)
        is_free = kwargs['context'].config_modifier.get_is_free()
        price_up = kwargs['context'].config_modifier.get_price_up()
        if not price_up and not is_free and kwargs['context'].config_gameplay.get_money() >= self.__cost:
            self.__create_tower(1, kwargs['context'].config_parameter_scene.get_height(), kwargs['context'])
            kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['is_filled'] = True
        elif price_up and not is_free and kwargs['context'].config_gameplay.get_money() >= self.__cost * 2:
            self.__create_tower(2, kwargs['context'].config_parameter_scene.get_height(), kwargs['context'])
            kwargs['context'].config_modifier.get_new_value_price_up(False)
            kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['is_filled'] = True
        elif is_free:
            self.__create_tower(0, kwargs['context'].config_parameter_scene.get_height(), kwargs['context'])
            kwargs['context'].config_modifier.get_new_value_price_up(False)
            kwargs['context'].config_modifier.get_new_value_is_free(False)
            kwargs['context'].maps_controller.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['is_filled'] = True

class ProductWithGun(ProductWithoutGun):
    def __init__(self, x, y, image, width, height, event, name, cost, damage, radius, improve_cost_array, armor_piercing, poison, image_gun):
        super().__init__(x, y, image, width, height, event, name, cost, damage, radius, improve_cost_array, armor_piercing, poison)
        self.__image_gun = image_gun

    def update(self, **kwargs):
        kwargs['context'].config_parameter_scene.get_screen().blit(self.__image_gun, self.rect)
        super().update(kwargs['context'])

    def __create_tower(self, price_coefficient, height, context):  # создает башню с характеристиками, зависящими от текущего тайла
        match context.maps_controller.get_build_array()[context.config_gameplay.get_current_tile()]['type']:
            case 1:
                self.__action(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context, image_gun=self.__image_gun)
            case 2:
                self.__action(
                    image=self.__image, damage=self.__damage_tower+1, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context, image_gun=self.__image_gun)
            case 3:
                self.__action(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower*1.2, height=height, context=context, image_gun=self.__image_gun)
            case 4:
                self.__action(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=True,
                    poison=self.__poison, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context, image_gun=self.__image_gun)
            case 5:
                self.__action(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison+1, additional_money=self.__additional_money, radius=self.__radius_tower, height=height, context=context, image_gun=self.__image_gun)
            case 6:
                self.__action(
                    image=self.__image, damage=self.__damage_tower, improve_array=self.__improve_cost_array, armor_piercing=self.__armor_piercing,
                    poison=self.__poison, additional_money=self.__additional_money+2, radius=self.__radius_tower, height=height, context=context, image_gun=self.__image_gun)
        context.config_gameplay.set_money(-self.__cost * price_coefficient)
'''