import TowerClass
import ButtonClass
from MainManu import  height

towers_object_array = []
button_update_array = []

def buy_tower(parameter_array):
    if parameter_array[0] is not None:
        print(parameter_array[0])
        parameter_array[1].append(TowerClass.Tower(parameter_array[2], parameter_array[3], parameter_array[4], parameter_array[5], parameter_array[6], parameter_array[7], parameter_array[0], parameter_array[8]))
    else:
        parameter_array[1].append(TowerClass.Tower(parameter_array[2], parameter_array[3], parameter_array[4], parameter_array[5], parameter_array[6], parameter_array[7], parameter_array[8]))
    return parameter_array[1]

def upgrade_tower(parameter_array):
    if towers_object_array[parameter_array[0]].level != 3:
        cost = towers_object_array[parameter_array[0]].improve_cost_array[towers_object_array[parameter_array[0]].level - 1]
        if parameter_array[1] >= cost:
            towers_object_array[parameter_array[0]].upgrade(1, 60)
            towers_object_array[parameter_array[0]].level += 1
            button_update_array[parameter_array[0]].change_image('images/upgrade/2lvl.png') if towers_object_array[parameter_array[0]].level == 2 else button_update_array[parameter_array[0]].change_image('images/upgrade/3lvl.png')
            parameter_array[1] -= cost
    return parameter_array[1]

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

    def buy(self, event, money, type_tile, is_free, scale_tower, coordinate_tower, tower_array, index, build_array, current_tile):
        if self.button_product.is_pressed(event) and (money >= self.cost or is_free):
            match type_tile:
                case 1:
                    self.button_product.handle_event_parameter([self.__additional_image, tower_array, self.__image, scale_tower, self.__damage_tower, coordinate_tower, index, self.__improve_cost_array, self.__radius_tower])
                    button_update_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                    build_array[current_tile]['is_filled'] = True
                    money -= self.cost
                case 2:
                    self.__damage_tower += 1
                    self.button_product.handle_event_parameter([self.__additional_image, tower_array, self.__image, scale_tower, self.__damage_tower, coordinate_tower, index, self.__improve_cost_array, self.__radius_tower])
                    button_update_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                    build_array[current_tile]['is_filled'] = True
                    money -= self.cost
                case 3:
                    self.__radius_tower = self.__radius_tower * 1.2
                    self.button_product.handle_event_parameter([self.__additional_image, tower_array, self.__image, scale_tower, self.__damage_tower, coordinate_tower, index, self.__improve_cost_array, self.__radius_tower])
                    button_update_array.append(ButtonClass.Button(height * 0.02, height - 37 * height / 150, 'images/upgrade/1lvl.png', 0.16 * height, 0.16 * height, upgrade_tower))
                    build_array[current_tile]['is_filled'] = True
                    money -= self.cost
        return money