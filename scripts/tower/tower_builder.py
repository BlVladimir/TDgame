from scripts.tower.tower_class import Tower
from scripts.tower.states_damage_maker import StateDamageMaker

class TowerBuilder:
    def __init__(self):
        self.__state_damage_maker = StateDamageMaker()

    def create_tower(self, type_tower:str, current_tile, context):
        return Tower(type_tower, current_tile.rect, context.tower_config.get_improve_cost_array(type_tower), self.__state_damage_maker.create_state(self.__make_characteristic(type_tower, current_tile, context)),
                     context.tower_config.get_gun_strategy(type_tower, current_tile.rect), context.tower_config.get_radius_strategy(type_tower, current_tile))

    @staticmethod
    def __make_characteristic(type_tower:str, current_tile, context)->dict:
        characteristic = context.tower_config.get_started_characteristic_dict(type_tower)
        current_tile.improve_characteristic(characteristic)
        return characteristic
