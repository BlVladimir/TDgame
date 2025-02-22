import TowerClass
from ButtonClass import Button


def buy_tower(parameter_dict):  # добавляет в массив башен новую
    height = parameter_dict['height']
    if 'additional_image' in parameter_dict.keys():
        parameter_dict['towers_controller'].append_tower_object(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'],
                                                                parameter_dict['coordinate'], parameter_dict['context'].get_config_gameplay().get_current_tile(),
                                                                parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], parameter_dict['additional_image'], parameter_dict['radius']),
                                                                Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
    else:
        parameter_dict['towers_controller'].append_tower_object(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'],
                                                                parameter_dict['coordinate'], parameter_dict['context'].get_config_gameplay().get_current_tile(),
                                                                parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], parameter_dict['radius']),
                                                                Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))

def upgrade_tower(parameter_dict):  # улучшение башни по номеру
    if parameter_dict['towers_controller'].get_current_tower().level != 3:
        cost =  parameter_dict['towers_controller'].get_current_tower().improve_cost_array[ parameter_dict['towers_controller'].get_current_tower().level - 1]
        is_free = parameter_dict['context'].get_config_modifier().get_is_free()
        price_up = parameter_dict['context'].get_config_modifier().get_price_up()
        if is_free:
            parameter_dict['towers_controller'].get_current_tower().upgrade(1, 60)
            parameter_dict['towers_controller'].get_current_tower().level += 1
            parameter_dict['towers_controller'].get_current_button_update().change_image('images/upgrade/2lvl.png') if  parameter_dict['towers_controller'].get_current_tower().level == 2 \
                else  parameter_dict['towers_controller'].get_current_button_update().change_image('images/upgrade/3lvl.png')
            parameter_dict['context'].get_config_modifier().get_new_value_is_free(False)
            parameter_dict['context'].get_config_modifier().get_new_value_price_up(False)
            parameter_dict['towers_controller'].append_upgrade(parameter_dict['context'], parameter_dict['maps_controller'])
        elif price_up and parameter_dict['context'].get_config_gameplay().get_money() >= cost * 2:
            parameter_dict['towers_controller'].get_current_tower().upgrade(1, 60)
            parameter_dict['towers_controller'].get_current_tower().level += 1
            parameter_dict['towers_controller'].get_current_button_update().change_image('images/upgrade/2lvl.png') if  parameter_dict['towers_controller'].get_current_tower().level == 2 \
                else  parameter_dict['towers_controller'].get_current_button_update().change_image('images/upgrade/3lvl.png')
            parameter_dict['context'].get_config_gameplay().new_value_money(-cost * 2)
            parameter_dict['context'].get_config_modifier().get_new_value_price_up(False)
            parameter_dict['towers_controller'].append_upgrade(parameter_dict['context'], parameter_dict['maps_controller'])
        elif not price_up and parameter_dict['context'].get_config_gameplay().get_money() >= cost:
            parameter_dict['towers_controller'].get_current_tower().upgrade(1, 60)
            parameter_dict['towers_controller'].get_current_tower().level += 1
            parameter_dict['towers_controller'].get_current_button_update().change_image('images/upgrade/2lvl.png') if  parameter_dict['towers_controller'].get_current_tower().level == 2 \
                else  parameter_dict['towers_controller'].get_current_button_update().change_image('images/upgrade/3lvl.png')
            parameter_dict['context'].get_config_gameplay().new_value_money(-cost)
            parameter_dict['towers_controller'].append_upgrade(parameter_dict['context'], parameter_dict['maps_controller'])


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
            self.button_product = Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)

        else:
            self.__additional_image = None
            self.button_product = Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

    def draw(self, context):  # рисует продукт
        self.button_product.draw(context)

    def __create_tower(self, type_tile, scale_tower, coordinate_tower, price_coefficient, height, towers_controller, context):  # создает башню с характеристиками, зависящими от текущего тайла
        match type_tile:
            case 1:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower, 'coordinate': coordinate_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower, 'height': height, 'towers_controller': towers_controller, 'context': context})
            case 2:
                self.__damage_tower += 1
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower, 'coordinate': coordinate_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower, 'height': height, 'towers_controller': towers_controller, 'context': context})
            case 3:
                self.__radius_tower = self.__radius_tower * 1.2
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,'coordinate': coordinate_tower, 'improve_array': self.__improve_cost_array,
                     'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower, 'height': height, 'towers_controller': towers_controller, 'context': context})
        context.get_config_gameplay().new_value_money(-self.cost * price_coefficient)


    def buy(self, event, type_tile, scale_tower, coordinate_tower, towers_controller, context):  # покупка башни
        is_free = context.get_config_modifier().get_is_free()
        price_up = context.get_config_modifier().get_price_up()
        is_filled = False
        if not price_up and not is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost:
            self.__create_tower(type_tile, scale_tower, coordinate_tower, 1, context.get_config_parameter_scene().get_height(), towers_controller, context)
            is_filled = True
        elif price_up and not is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost * 2:
            self.__create_tower(type_tile, scale_tower, coordinate_tower, 2, context.get_config_parameter_scene().get_height(), towers_controller, context)
            context.get_config_modifier().get_new_value_price_up(False)
            is_filled = True
        elif is_free and self.button_product.is_pressed(event) and context.get_config_gameplay().get_money() >= self.cost * 2:
            self.__create_tower(type_tile, scale_tower, coordinate_tower, 0, context.get_config_parameter_scene().get_height(), towers_controller, context)
            context.get_config_modifier().get_new_value_price_up(False)
            context.get_config_modifier().get_new_value_is_free(False)
            is_filled = True
        return is_filled