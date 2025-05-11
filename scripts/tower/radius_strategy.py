import abc
import math

class AbstractRadiusStrategy(abc.ABC):
    @abc.abstractmethod
    def is_in_radius(self, coordinate_center) -> bool:
        pass

class RoundRadius(AbstractRadiusStrategy):
    def __init__(self, radius, coordinate_center_tower):
        self.__radius = radius
        self.__coordinate_center_tower = coordinate_center_tower

    def is_in_radius(self, coordinate_center):
        if (self.__coordinate_center_tower[0] - coordinate_center[0]) ** 2 + (self.__coordinate_center_tower[1] - coordinate_center[1]) ** 2 <= self.__radius**2:  # если башня не использованная и координаты центра врага в радиусе башни
            return True
        else:
            return False

class InfinityRadius(AbstractRadiusStrategy):
    def is_in_radius(self, coordinate_center):
        return True