import TowerClass
import ButtonClass


def buy_tower(parameter_dict):  # добавляет в массив башен новую
    tower_array = parameter_dict['context'].get_config_shop().get_towers_object_array()
    if 'additional_image' in parameter_dict.keys():
        tower_array.append(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'],
                                                                parameter_dict['coordinate'], parameter_dict['index'],
                                                                parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], parameter_dict['additional_image'], parameter_dict['radius']))
    else:
        tower_array.append(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'],
                                                                parameter_dict['coordinate'], parameter_dict['index'],
                                                                parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], parameter_dict['radius']))
    parameter_dict['context'].get_config_shop().new_value_towers_object_array(tower_array)

def upgrade_tower(context):  # улучшение башни по номеру
    tower_array = context.get_config_shop().get_towers_object_array()
    button_array = context.get_config_shop().get_button_update_array()
    current_tower = context.get_config_gameplay().get_current_tower()
    if tower_array[current_tower].level != 3:
        cost = tower_array[current_tower].improve_cost_array[tower_array[current_tower].level - 1]
        is_free = context.get_config_modifier().get_is_free()
        price_up = context.get_config_modifier().get_price_up()
        if is_free:
            tower_array[current_tower].upgrade(1, 60)
            tower_array[current_tower].level += 1
            button_array[current_tower].change_image('images/upgrade/2lvl.png') if tower_array[current_tower].level == 2 \
                else button_array[current_tower].change_image('images/upgrade/3lvl.png')
            context.get_config_modifier().get_new_value_is_free(False)
            context.get_config_modifier().get_new_value_price_up(False)
        elif price_up and context.get_config_gameplay().get_money() >= cost * 2:
            tower_array[current_tower].upgrade(1, 60)
            tower_array[current_tower].level += 1
            button_array[current_tower].change_image('images/upgrade/2lvl.png') if tower_array[current_tower].level == 2 \
                else button_array[current_tower].change_image('images/upgrade/3lvl.png')
            context.get_config_gameplay().new_value_money(-cost * 2)
            context.get_config_modifier().get_new_value_price_up(False)
        elif not price_up and context.get_config_gameplay().get_money() >= cost:
            tower_array[current_tower].upgrade(1, 60)
            tower_array[current_tower].level += 1
            button_array[current_tower].change_image('images/upgrade/2lvl.png') if tower_array[current_tower].level == 2 \
                else button_array[current_tower].change_image('images/upgrade/3lvl.png')
            context.get_config_gameplay().new_value_money(-cost)
    context.get_config_shop().new_value_towers_object_array(tower_array)
    context.get_config_shop().new_value_button_update_array(button_array)


class Product:  # класс продуктов
    def __init__(self, image, cost, scale, coordinate, damage, radius, improve_cost_array, armor_piercing, poison, additional_image = None):
        self.__image = image
        self.cost = cost
        self.armor_piercing = armor_piercing
        self.poison = poison
        self.__damage_tower = damage
        self.__radius_tower = radius
        self.__improve_cost_array = improve_cost_array
        self.coordinate = coordinate
        self.scale = scale
        if additional_image is not None:  # нужно, так как не у всех башен есть вращающаяся пушка
            self.__additional_image = additional_image
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)

        else:
            self.__additional_image = None
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

    def draw(self, screen):  # рисует продукт
        self.button_product.draw(screen)

    def __create_tower(self, type_tile, scale_tower, coordinate_tower, index, build_array, current_tile, price_coefficient, height, context):  # создает башню с характеристиками, зависящими от текущего тайла
        button_array = context.get_config_shop().get_button_update_array()
        button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
        context.get_config_shop().new_value_button_update_array(button_array)
        match type_tile:
            case 1:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                     'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower, 'context': context})
                build_array[current_tile]['is_filled'] = True
            case 2:
                self.__damage_tower += 1
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                     'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower, 'context': context})
                build_array[current_tile]['is_filled'] = True
            case 3:
                self.__radius_tower = self.__radius_tower * 1.2
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                     'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower, 'context': context})
                build_array[current_tile]['is_filled'] = True
        context.get_config_gameplay().new_value_money(-self.cost * price_coefficient)

    def buy(self, event, type_tile, scale_tower, coordinate_tower, index, build_array, current_tile, context):  # покупка башни
        is_free = context.get_config_modifier().get_is_free()
        price_up = context.get_config_modifier().get_price_up()
        if not price_up and not is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost:
            self.__create_tower(type_tile, scale_tower, coordinate_tower, index,  build_array, current_tile, 1, context.get_config_parameter_scene().get_height(), context)
        elif price_up and not is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost * 2:
            self.__create_tower(type_tile, scale_tower, coordinate_tower, index, build_array, current_tile, 2, context.get_config_parameter_scene().get_height(), context)
            context.get_config_modifier().get_new_value_price_up(False)
        elif is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost * 2:
            self.__create_tower(type_tile, scale_tower, coordinate_tower, index, context.get_config_shop().get_button_update_array(), build_array, current_tile, 0, context)
            context.get_config_modifier().get_new_value_price_up(False)
            context.get_config_modifier().get_new_value_is_free(False)
        return build_array