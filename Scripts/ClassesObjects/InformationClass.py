import pygame
from Scripts.MainScripts import Function


def get_coordinate_list(interval_x, interval_y, value_lines, coordinate):  # получает список координат из интервала x и y и количества строк
    height_one_line = interval_y / value_lines
    coordinate_list = []
    for i in range(value_lines):
        coordinate_list.append((coordinate[0] + interval_x/2, int(height_one_line * (i + 0.5) + coordinate[1])))
    return coordinate_list


class Information:
    def __init__(self, height, width):
        self.__coordinate = (width - 0.4 * height, 0)
        self.__image = pygame.transform.scale(pygame.image.load('images/UI/shopBackground.png'), (height * 0.4, height))
        self.__modifier_array = ('free purchase', 'price up', 'health', 'money', 'damage')
        self.__current_modifier = []


    def __draw_characteristic(self, height, context):  # рисует характеристики врага
        if context.get_enemies_controller().get_current_enemy() is not None:
            health_line = 'health ' + str(context.get_enemies_controller().get_current_enemy().health)
            context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(pygame.image.load('images/UI/enemyСharacteristic/health.png'), (int(height * 0.08), int(height * 0.08))), (self.__coordinate[0] + height * 0.4 * 0.1, height * 0.04))
            Function.draw_text_from_center(health_line, int(height * 0.08), (self.__coordinate[0] + height * 0.4 * 0.7, height * 0.15), context)

    def draw(self, height, width, context):  # рисует панель информации
        context.get_config_parameter_scene().get_screen().blit(self.__image, self.__coordinate)
        context.get_config_parameter_scene().get_screen().blit(pygame.transform.scale(pygame.image.load('images/UI/enemyСharacteristic/bugs.png'), (height * 0.4, height * 0.2)), (self.__coordinate[0], height * 0.2))
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

    def draw_bugs(self, height, width, context):  # рисует массив модификаторов
        is_free = context.get_config_modifier().get_is_free()
        price_up = context.get_config_modifier().get_price_up()
        type_modifier = context.get_config_modifier().get_type_new_modifier()
        influence = context.get_config_modifier().get_influence()
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
                    context.get_config_modifier().get_new_value_type_new_modifier(None)
                    context.get_config_modifier().get_new_value_influence(None)
                elif influence == 1:
                    self.__change_modifier_array(self.__modifier_array[4] + ' + 1')
                    context.get_config_modifier().get_new_value_type_new_modifier(None)
                    context.get_config_modifier().get_new_value_influence(None)
            case 2:
                if influence == 0:
                    self.__change_modifier_array(self.__modifier_array[2] + ' + 1')
                    context.get_config_modifier().get_new_value_type_new_modifier(None)
                    context.get_config_modifier().get_new_value_influence(None)
                elif influence == 1:
                    self.__change_modifier_array(self.__modifier_array[2] + ' - 1')
                    context.get_config_modifier().get_new_value_type_new_modifier(None)
                    context.get_config_modifier().get_new_value_influence(None)
            case 3:
                if influence == 0:
                    self.__change_modifier_array(self.__modifier_array[3] + ' - 1')
                    context.get_config_modifier().get_new_value_type_new_modifier(None)
                    context.get_config_modifier().get_new_value_influence(None)
                elif influence == 1:
                    self.__change_modifier_array(self.__modifier_array[3] + ' + 1')
                    context.get_config_modifier().get_new_value_type_new_modifier(None)
                    context.get_config_modifier().get_new_value_influence(None)

        if len(self.__current_modifier) != 0:
            coordinate_array = get_coordinate_list(height * 0.38, height * 0.58, len(self.__current_modifier), (width - height * 0.39, height * 0.41))
            for i in range(len(self.__current_modifier)):
                Function.draw_text_from_center(self.__current_modifier[i], 50, coordinate_array[i], context)


