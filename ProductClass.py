import TowerClass
import ButtonClass
from MainManu import  height


def buy_tower(parameter_dict):
    if 'additional_image' in parameter_dict.keys():
        parameter_dict['tower_array'].append(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'], parameter_dict['coordinate'], parameter_dict['index'],
                                                              parameter_dict['improve_array'], parameter_dict['additional_image'], parameter_dict['radius']))
    else:
        parameter_dict['tower_array'].append(TowerClass.Tower(parameter_dict['image'], parameter_dict['scale'], parameter_dict['damage'], parameter_dict['coordinate'], parameter_dict['index'],
                                                              parameter_dict['improve_array'], parameter_dict['radius']))
    return parameter_dict['tower_array']

def upgrade_tower(parameter_dict):
    if parameter_dict['tower_array'][parameter_dict['level']].level != 3:
        cost = parameter_dict['tower_array'][parameter_dict['number']].improve_cost_array[parameter_dict['tower_array'][parameter_dict['level']].level - 1]
        if parameter_dict['money'] >= cost:
            parameter_dict['tower_array'][parameter_dict['number']].upgrade(1, 60)
            parameter_dict['tower_array'][parameter_dict['number']].level += 1
            parameter_dict['button_array'][parameter_dict['number']].change_image('images/upgrade/2lvl.png') if parameter_dict['tower_array'][parameter_dict['level']].level == 2 \
                else parameter_dict['button_array'][parameter_dict[0]].change_image('images/upgrade/3lvl.png')
            parameter_dict['money'] -= cost
    return parameter_dict['money']

class Product:
    def __init__(self, image, cost, scale, coordinate, damage, radius, improve_cost_array, additional_image = None):
        self.__image = image
        self.cost = cost
        self.__damage_tower = damage
        self.__radius_tower = radius
        self.__improve_cost_array = improve_cost_array
        self.coordinate = coordinate
        self.scale = scale
        if additional_image is not None:
            self.__additional_image = additional_image
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)

        else:
            self.__additional_image = None
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

    def draw(self, screen):
        self.button_product.draw(screen)

    def buy(self, event, tower_array, button_array, money, type_tile, is_free, scale_tower, coordinate_tower, index, build_array, current_tile):
        if self.button_product.is_pressed(event) and (money >= self.cost or is_free):
            match type_tile:
                case 1:
                    tower_array = self.button_product.handle_event_parameter({'additional_image': self.__additional_image, 'tower_array': tower_array, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                                                                              'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'radius': self.__radius_tower})
                    button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                    build_array[current_tile]['is_filled'] = True
                    money -= self.cost
                case 2:
                    self.__damage_tower += 1
                    tower_array = self.button_product.handle_event_parameter({'additional_image':self.__additional_image, 'tower_array':tower_array, 'image':self.__image, 'scale':scale_tower, 'damage':self.__damage_tower,
                                                                              'coordinate':coordinate_tower, 'index':index, 'improve_array':self.__improve_cost_array, 'radius':self.__radius_tower})
                    button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                    build_array[current_tile]['is_filled'] = True
                    money -= self.cost
                case 3:
                    self.__radius_tower = self.__radius_tower * 1.2
                    tower_array = self.button_product.handle_event_parameter({'additional_image': self.__additional_image, 'tower_array': tower_array, 'image': self.__image, 'scale': scale_tower, 'damage': self.__damage_tower,
                                                                              'coordinate': coordinate_tower, 'index': index, 'improve_array': self.__improve_cost_array, 'radius': self.__radius_tower})
                    button_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                    build_array[current_tile]['is_filled'] = True
                    money -= self.cost
        return money, build_array, tower_array