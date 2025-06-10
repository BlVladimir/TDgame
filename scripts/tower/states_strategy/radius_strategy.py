import abc

class AbstractRadiusStrategy(abc.ABC):
    def __init__(self, radius:float):
        self.__radius = radius

    @abc.abstractmethod
    def is_in_radius(self, coordinate_center) -> bool:
        pass

    def multiply_radius(self, value):
        self.__radius *= value

    def upgrade(self, visitor):
        visitor.visit_radius_strategy(self)

    def clone(self, tile):
        if tile.improved_characteristic == 'radius':
            c = tile.velue
        else:
            c = 1
        new = self.__class__(self.__radius*c)
        return new

    @property
    def radius(self):
        return self.__radius

class RoundRadius(AbstractRadiusStrategy):
    def __init__(self, radius:float, coordinate_center_tower=(0, 0)):
        super().__init__(radius)
        self.__coordinate_center_tower = coordinate_center_tower

    def is_in_radius(self, coordinate_center):
        if (self.__coordinate_center_tower[0] - coordinate_center[0]) ** 2 + (self.__coordinate_center_tower[1] - coordinate_center[1]) ** 2 <= super().radius**2:  # если башня не использованная и координаты центра врага в радиусе башни
            return True
        else:
            return False

    def clone(self, tile):
        if tile.improved_characteristic == 'radius':
            c = tile.velue
        else:
            c = 1
        new = self.__class__(self.__radius*c, tile.rect.center)
        return new


class InfinityRadius(AbstractRadiusStrategy):
    def __init__(self):
        super().__init__(0)

    def is_in_radius(self, coordinate_center=(0, 0)):
        return True