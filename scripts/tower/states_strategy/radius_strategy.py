import abc

class AbstractRadiusStrategy(abc.ABC):
    def __init__(self, radius):
        self.__radius = radius

    @abc.abstractmethod
    def is_in_radius(self, coordinate_center) -> bool:
        pass

    def multiply_radius(self, value):
        self.__radius *= value

    def upgrade(self, visitor):
        visitor.visit_radius_strategy(self)

    @property
    def radius(self):
        return self.__radius

class RoundRadius(AbstractRadiusStrategy):
    def __init__(self, radius, coordinate_center_tower):
        super().__init__(radius)
        self.__coordinate_center_tower = coordinate_center_tower

    def is_in_radius(self, coordinate_center):
        if (self.__coordinate_center_tower[0] - coordinate_center[0]) ** 2 + (self.__coordinate_center_tower[1] - coordinate_center[1]) ** 2 <= super().radius**2:  # если башня не использованная и координаты центра врага в радиусе башни
            return True
        else:
            return False

class InfinityRadius(AbstractRadiusStrategy):
    def __init__(self):
        super().__init__(0)

    def is_in_radius(self, coordinate_center=(0, 0)):
        return True