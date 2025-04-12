import pygame
from scripts.main_scripts import function


def get_coordinate_list(interval_x, interval_y, value_lines, coordinate, t = 0):  # получает список координат из интервала x и y и количества строк
    height_one_line = interval_y / value_lines
    coordinate_list = []
    if t == 0:  # по умолчанию центральная координата, иначе координата верхнего левого угла
        for i in range(value_lines):
            coordinate_list.append((coordinate[0] + interval_x/2, int(height_one_line * (i + 0.5) + coordinate[1])))
    else:
        for i in range(value_lines):
            coordinate_list.append((coordinate[0], int(height_one_line * (i + 0.5) + coordinate[1])))
    return coordinate_list



class Information:
    def __init__(self, height, width):
        self.__coordinate = (width - 0.4 * height, 0)
        self.__image = pygame.transform.scale(pygame.image.load('images/UI/shop_background.png'), (height * 0.4, height))
        self.__modifier_array = ('free purchase', 'price up', 'health', 'money', 'damage')
        self.__image_characteristic_dict = {'health': pygame.image.load('images/UI/enemy_characteristic/health.png'),
                                           'price': pygame.image.load('images/UI/money.png'),
                                           'healing': pygame.image.load('images/UI/enemy_characteristic/healing.png'),
                                           'armor': pygame.image.load('images/UI/enemy_characteristic/shield.png'),
                                           'poison': pygame.image.load('images/UI/enemy_characteristic/poison.png')}
        self.__current_modifier = []
        for i in self.__image_characteristic_dict.keys():
            self.__image_characteristic_dict[i] = pygame.transform.scale(self.__image_characteristic_dict[i], (height * 0.05, height * 0.05))

    def __draw_characteristic(self, height, context):  # рисует характеристики врага
        if context.enemies_controller.get_current_enemy() is not None:
            characteristic_dict = context.enemies_controller.get_current_enemy().get_characteristic()
            coordinate_array = get_coordinate_list(height * 0.38, height * 0.38, len(characteristic_dict), (context.config_parameter_scene.get_width() - height * 0.39, height * 0.01), 1)
            i = 0
            for j in characteristic_dict.keys():
                context.config_parameter_scene.get_screen().blit(self.__image_characteristic_dict[j], (coordinate_array[i][0] + context.config_parameter_scene.get_height() * 0.08, coordinate_array[i][1]))
                function.draw_text(characteristic_dict[j], int(context.config_parameter_scene.get_height() * 0.06), (coordinate_array[i][0] + context.config_parameter_scene.get_height() * 0.15, coordinate_array[i][1]), context, 1)
                i += 1


    def draw(self, height, width, context):  # рисует панель информации
        context.config_parameter_scene.get_screen().blit(self.__image, self.__coordinate)
        context.config_parameter_scene.get_screen().blit(pygame.transform.scale(pygame.image.load('images/UI/enemy_characteristic/bugs.png'), (height * 0.4, height * 0.2)), (self.__coordinate[0], height * 0.4))
        self.__draw_characteristic(height, context)
        self.draw_bugs(height, width, context)

    def __change_modifier_array(self, text):  # меняет массив модификаторов
        if self.__current_modifier:
            if self.__current_modifier[0] == self.__modifier_array[0] or self.__current_modifier[0] == self.__modifier_array[1]:
                if text == self.__modifier_array[0] and self.__current_modifier[0] == self.__modifier_array[1]:
                    self.__current_modifier[0] = text
                elif text != self.__modifier_array[0] and text != self.__modifier_array[1]:
                    self.__current_modifier.insert(1, text)
            else:
                self.__current_modifier.insert(0, text)
            if len(self.__current_modifier) > 4:
                self.__current_modifier.pop(len(self.__current_modifier) - 1)
        else:
            self.__current_modifier.append(text)

    def reset_modifier(self):  # сбрасывает модификаторы
        self.__current_modifier = []

    def draw_bugs(self, height, width, context):  # рисует массив модификаторов
        is_free = context.config_modifier.get_is_free()
        price_up = context.config_modifier.get_price_up()
        type_modifier = context.config_modifier.get_type_new_modifier()
        influence = context.config_modifier.get_influence()
        if is_free:
            self.__change_modifier_array(self.__modifier_array[0])
        elif price_up:
            self.__change_modifier_array(self.__modifier_array[1])
        else:
            if self.__current_modifier and (self.__current_modifier[0] == self.__modifier_array[0] or self.__current_modifier[0] == self.__modifier_array[1]):
                self.__current_modifier.pop(0)
        match type_modifier:
            case 1:
                if influence == 0:
                    self.__change_modifier_array(self.__modifier_array[4] + ' - 1')
                    context.config_modifier.get_new_value_type_new_modifier(None)
                    context.config_modifier.get_new_value_influence(None)
                elif influence == 1:
                    self.__change_modifier_array(self.__modifier_array[4] + ' + 1')
                    context.config_modifier.get_new_value_type_new_modifier(None)
                    context.config_modifier.get_new_value_influence(None)
            case 2:
                if influence == 0:
                    self.__change_modifier_array(self.__modifier_array[2] + ' + 1')
                    context.config_modifier.get_new_value_type_new_modifier(None)
                    context.config_modifier.get_new_value_influence(None)
                elif influence == 1:
                    self.__change_modifier_array(self.__modifier_array[2] + ' - 1')
                    context.config_modifier.get_new_value_type_new_modifier(None)
                    context.config_modifier.get_new_value_influence(None)
            case 3:
                if influence == 0:
                    self.__change_modifier_array(self.__modifier_array[3] + ' - 1')
                    context.config_modifier.get_new_value_type_new_modifier(None)
                    context.config_modifier.get_new_value_influence(None)
                elif influence == 1:
                    self.__change_modifier_array(self.__modifier_array[3] + ' + 1')
                    context.config_modifier.get_new_value_type_new_modifier(None)
                    context.config_modifier.get_new_value_influence(None)
        if len(self.__current_modifier) != 0:
            coordinate_array = get_coordinate_list(height * 0.38, height * 0.38, len(self.__current_modifier), (width - height * 0.39, height * 0.61))
            for i in range(len(self.__current_modifier)):
                function.draw_text(self.__current_modifier[i], int(height * 0.06), coordinate_array[i], context)