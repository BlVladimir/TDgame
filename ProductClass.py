import TowerClass
import ButtonClass
from MainManu import  height


def buy_tower(parameter_dict):  # добавляет в массив башен новую
    if 'additional_image' in parameter_dict.keys():
        parameter_dict['tower_array'].append(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'], parameter_dict['coordinate'], parameter_dict['index'],
                                                              parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], parameter_dict['additional_image'], parameter_dict['radius']))
    else:
        parameter_dict['tower_array'].append(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'], parameter_dict['coordinate'], parameter_dict['index'],
                                                              parameter_dict['improve_array'], parameter_dict['armor_piercing'], parameter_dict['poison'], parameter_dict['radius']))

def upgrade_tower(parameter_dict):  # улучшение башни по номеру
    if parameter_dict['tower_array'][parameter_dict['number']].level != 3:
        cost = parameter_dict['tower_array'][parameter_dict['number']].improve_cost_array[parameter_dict['tower_array'][parameter_dict['number']].level - 1]
        if parameter_dict['is_free']:
            parameter_dict['tower_array'][parameter_dict['number']].upgrade(1, 60)
            parameter_dict['tower_array'][parameter_dict['number']].level += 1
            parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/2lvl.png') if parameter_dict['tower_array'][parameter_dict['number']].level == 2 \
                else parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/3lvl.png')
            parameter_dict['is_free'] = False
            parameter_dict['price_up'] = False
        elif parameter_dict['price_up'] and parameter_dict['money'] >= cost * 2:
            parameter_dict['tower_array'][parameter_dict['number']].upgrade(1, 60)
            parameter_dict['tower_array'][parameter_dict['number']].level += 1
            parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/2lvl.png') if parameter_dict['tower_array'][parameter_dict['number']].level == 2 \
                else parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/3lvl.png')
            parameter_dict['money'] -= cost * 2
            parameter_dict['price_up'] = False
        elif not parameter_dict['price_up'] and parameter_dict['money'] >= cost:
            parameter_dict['tower_array'][parameter_dict['number']].upgrade(1, 60)
            parameter_dict['tower_array'][parameter_dict['number']].level += 1
            parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/2lvl.png') if parameter_dict['tower_array'][parameter_dict['number']].level == 2 \
                else parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/3lvl.png')
            parameter_dict['money'] -= cost
    return parameter_dict['money'], parameter_dict['is_free'], parameter_dict['price_up']


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

    def draw(self, screen):
        self.button_product.draw(screen)

    def __create_tower(self, type_tile, tower_array, scale_tower, coordinate_tower, index, button_array, build_array, current_tile, money, price_coefficient):  # различные параметры, в зависимости от текущего тайла
        match type_tile:
            case 1:
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'tower_array': tower_array, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                     'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower})
                button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                build_array[current_tile]['is_filled'] = True
                money -= self.cost * price_coefficient
            case 2:
                self.__damage_tower += 1
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'tower_array': tower_array, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                     'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower})
                button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                build_array[current_tile]['is_filled'] = True
                money -= self.cost * price_coefficient
            case 3:
                self.__radius_tower = self.__radius_tower * 1.2
                self.button_product.handle_event_parameter(
                    {'additional_image': self.__additional_image, 'tower_array': tower_array, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                     'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'armor_piercing': self.armor_piercing, 'poison': self.poison, 'radius': self.__radius_tower})
                button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                build_array[current_tile]['is_filled'] = True
                money -= self.cost * price_coefficient
        return money

    def buy(self, event, tower_array, button_array, money, type_tile, is_free, price_up, scale_tower, coordinate_tower, index, build_array, current_tile):  # покупка
        if not price_up and not is_free and self.button_product.is_pressed(event) and money >= self.cost:
            money = self.__create_tower(type_tile, tower_array, scale_tower, coordinate_tower, index, button_array, build_array, current_tile, money, 1)
        elif price_up and not is_free and self.button_product.is_pressed(event) and money >= self.cost * 2:
            money = self.__create_tower(type_tile, tower_array, scale_tower, coordinate_tower, index, button_array, build_array, current_tile, money, 2)
            price_up = False
        elif is_free and self.button_product.is_pressed(event) and money >= self.cost * 2:
            money = self.__create_tower(type_tile, tower_array, scale_tower, coordinate_tower, index, button_array, build_array, current_tile, money, 0)
            price_up = False
            is_free = True
        return money, build_array, is_free, price_up