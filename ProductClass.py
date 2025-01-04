import TowerClass
import ButtonClass

def buy_tower(additional_image, image, scale,tower_array, damage, radius, coordinate, index, improve_cost_array):
    if additional_image is not None:
        tower_array.append(TowerClass.Tower(image, scale, damage, coordinate, index, improve_cost_array, radius, additional_image))
    else:
        tower_array.append(TowerClass.Tower(image, scale, damage, coordinate, index, improve_cost_array, radius))
    return tower_array

class Product:
    def __init__(self, image, cost, scale, coordinate, additional_image = None):
        self.__image = image
        self.cost = cost
        if additional_image is not None:
            self.__additional_image = additional_image
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower, additional_image)

        else:
            self.__additional_image = None
            self.button_product = ButtonClass.Button(coordinate[0], coordinate[1], image, scale, scale, buy_tower)

