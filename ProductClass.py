import TowerClass

class Product:
    def __init__(self, image, cost, scale, additional_image = None):
        self.__image = image
        self.__scale = scale
        self.cost = cost
        if additional_image is not None:
            self.__additional_image = additional_image

    def buy_tower(self, tower_array):
        tower_array.append(TowerClass.Tower(self.__image, self.__scale))