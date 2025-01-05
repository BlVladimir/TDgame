import TowerClass
import ButtonClass


def buy_tower(parameter_array):
    if parameter_array[0] is not None:
        parameter_array[1].append(TowerClass.Tower(parameter_array[2], parameter_array[3], parameter_array[4], parameter_array[5], parameter_array[6], parameter_array[7], parameter_array[8], parameter_array[0]))
    else:
        parameter_array[1].append(TowerClass.Tower(parameter_array[2], parameter_array[3], parameter_array[4], parameter_array[5], parameter_array[6], parameter_array[7], parameter_array[8]))
    return parameter_array[1]

class Product:
    def __init__(self, image, cost, scale, coordinate, damage, radius, improve_cost_array, additional_image = None):
        self.__image = image
        self.cost = cost
        self.__damage_tower = damage
        self.__radius_tower = radius
        self.__improve_cost_array = improve_cost_array
        if additional_image is not None:
            self.__additional_image = additional_image
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)

        else:
            self.__additional_image = None
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

    def draw(self, screen):
        self.button_product.draw(screen)

    def buy(self, event, money, type_tile, is_free, scale_tower, coordinate_tower, tower_array, index):
        if self.button_product.is_pressed(event) and (money >= self.cost or is_free):
            match type_tile:
                case 2:
                    self.__damage_tower += 1
                    self.button_product.handle_event_parameter([self.__additional_image, tower_array, self.__image, scale_tower, self.__damage_tower, coordinate_tower, index, self.__improve_cost_array, self.__radius_tower])
                case 3:
                    self.__radius_tower = self.__radius_tower * 1.2
                    self.button_product.handle_event_parameter([self.__additional_image, tower_array, self.__image, scale_tower, self.__damage_tower, coordinate_tower, index, self.__improve_cost_array, self.__radius_tower])