from scripts.tower.states_strategy.state_damage import StateDamage

class StateDamageMaker:
    def __init__(self):
        self.__priority_array = ('addition_money', 'basic_damage', 'poison', 'armor_piercing')
        self.__func_dict = {'poison':self.__poison_func,
                            'armor_piercing':self.__piercing_armor_func,
                            'basic_damage':self.__basic_damage_func,
                            'addition_money':self.__addition_money}

    @staticmethod

    def __basic_damage_func(enemy, func=None, **kwargs):
        enemy.reduce_health_with_armor(kwargs['damage'])
        func(enemy, kwargs)

    @staticmethod
    def __poison_func(enemy, func=None, **kwargs):
        enemy.to_poison(kwargs['poison_damage'])
        func(enemy, kwargs)

    @staticmethod
    def __piercing_armor_func(enemy, func=None, **kwargs):
        enemy.reduce_health(kwargs['damage'])
        func(enemy, kwargs)

    @staticmethod
    def __addition_money(enemy, func=None, **kwargs):
        enemy.increase_additional_money(kwargs['additional_money'])
        func(enemy, kwargs)

    def create_state(self, characteristic_dict:dict):
        states = []
        for i in self.__priority_array:
            if i in characteristic_dict.keys():
                states.append(i)
        func_array = []
        for i in states:
            func_array.append(self.__func_dict[i])
        return StateDamage(states[0], func_array, characteristic_dict)
