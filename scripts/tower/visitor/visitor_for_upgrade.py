from scripts.tower.states_strategy.state_damage import StateDamage
from scripts.tower.states_strategy.radius_strategy import AbstractRadiusStrategy

class VisitorForUpgrade:
    def __init__(self, **upgrade_parameters):
        self.__upgrade_parameters = upgrade_parameters
        self.__current_level = 0

    def visit_damage_state(self, damage_state:StateDamage):
        for i in self.__upgrade_parameters.keys():
            damage_state.improve_damage(i, self.__upgrade_parameters[i])

    def visit_radius_strategy(self, radius_strategy:AbstractRadiusStrategy):
        radius_strategy.multiply_radius(self.__upgrade_parameters['radius'])

    @property
    def current_level(self):
        raise PermissionError('privet attribute')

    @current_level.setter
    def current_level(self, value):
        self.__current_level = value