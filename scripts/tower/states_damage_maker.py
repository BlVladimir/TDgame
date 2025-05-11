from scripts.main_scripts.resourse_path import resource_path
from scripts.tower.state_damage import StateDamage, StateDamageWithAnimatedBullet
import pygame

class StateDamageMaker:
    def __init__(self):
        self.__priority_dict = {'poison':1,
                                'piercing_armor':2,
                                'common':0,
                                'addition_money':-1}
        self.__func_dict = {'poison':self.__poison_func,
                            'piercing_armor':self.__piercing_armor_func,
                            'common':self.__common_func,
                            'addition_money':self.__addition_money}
        self.__images_bullets_dict = {'poison':'animation_poison_bullet',
                                      'piercing_armor':'animation_electric_bullet',
                                      'common':pygame.image.load(resource_path('images/tower/Bullets/common_bullet.png'))}

    @staticmethod
    def __common_func(enemy, func=None, **kwargs):
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

    def __sort_by_priority(self, states):
        for i in states:
            if i not in self.__priority_dict.keys():
                raise ValueError(f'{i} is not state')
        flag = True
        while flag:
            flag = False
            for i in range(len(states) - 1):
                if self.__priority_dict[states[i]] < self.__priority_dict[states[i + 1]]:
                    states[i], states[i + 1] = states[i + 1], states[i]
                    flag = True
        return states

    def create_state(self, *args, **kwargs):
        states = self.__sort_by_priority(args)
        func_array = []
        for i in states:
            func_array.append(self.__func_dict[i])
        match states[0]:
            case 'common':
                return StateDamage(func_array, self.__images_bullets_dict['common'], kwargs)
            case _:
                return StateDamageWithAnimatedBullet(func_array, self.__images_bullets_dict[states[0]], kwargs)
