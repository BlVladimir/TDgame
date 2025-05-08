from sys import exit
from scripts.classes_objects.tower_class import Tower
import json

def buy_tower(**kwargs):
    if 'additional_image' in kwargs.keys():
        kwargs['context'].towers_array_iterator.append_tower_object(
            Tower(kwargs['image'], kwargs['context'].maps_array_iterator.get_tile_scale(), kwargs['damage'],
                  kwargs['context'].maps_array_iterator.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'],
                  kwargs['context'].config_gameplay.get_current_tile(),
                  kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], image_gun=kwargs['additional_image'],
                  radius=kwargs['radius']))
    else:
        kwargs['context'].towers_array_iterator.append_tower_object(
            Tower(kwargs['image'], kwargs['context'].maps_array_iterator.get_tile_scale(), kwargs['damage'],
                  kwargs['context'].maps_array_iterator.get_build_array()[kwargs['context'].config_gameplay.get_current_tile()]['coordinate'],
                  kwargs['context'].config_gameplay.get_current_tile(),
                  kwargs['improve_array'], kwargs['armor_piercing'], kwargs['poison'], radius=kwargs['radius']))

class EventController:
    def __init__(self):
        self.__products = json.dumps({'common': dict(image="images/tower/common_foundation.png", damage=2, cost=3, radius=1, improve_cost_array=(4, 6), armor_piercing=False, poison=0, additional_money=2,
                                  additional_image="images/tower/common_gun.png"),
                   'sniper': dict(image="images/tower/common_foundation.png", damage=4, cost=5, radius=2, improve_cost_array=(6, 8), armor_piercing=False, poison=0, additional_money=0,
                                  additional_image="images/tower/sniper_gun.png"),
                   'anty_shield': dict(image="images/tower/anty_shield.png", damage=3, cost=4, radius=1.5, improve_cost_array=(5, 7), armor_piercing=True, poison=0, additional_money=0),
                   'venom': dict(image="images/tower/venom_foundation.png", damage=2, cost=5, radius=1, improve_cost_array=(4, 6), armor_piercing=False, poison=2, additional_money=0,
                                 additional_image="images/tower/venom_gun.png")})

    def __create_tower(self, price_coefficient, context, type):  # создает башню с характеристиками, зависящими от текущего тайла
        characteristic = json.loads(self.__products)[type]
        match context.maps_array_iterator.get_build_array()[context.config_gameplay.get_current_tile()]['type']:
            case 1:
                buy_tower(
                    image=characteristic['image'], damage=characteristic['damage'], improve_array=characteristic['improve_cost_array'], armor_piercing=characteristic['armor_piercing'],
                    poison=characteristic['poison'], additional_money=characteristic['additional_money'], radius=characteristic['radius'], context=context)
            case 2:
                buy_tower(
                    image=characteristic['image'], damage=characteristic['damage'] + 1, improve_array=characteristic['improve_cost_array'], armor_piercing=characteristic['__armor_piercing'],
                    poison=characteristic['poison'], additional_money=characteristic['additional_money'], radius=characteristic['radius'], context=context)
            case 3:
                buy_tower(
                    image=characteristic['image'], damage=characteristic['damage'], improve_array=characteristic['improve_cost_array'], armor_piercing=characteristic['armor_piercing'],
                    poison=characteristic['poison'], additional_money=characteristic['additional_money'], radius=characteristic['radius'] * 1.2, context=context)
            case 4:
                buy_tower(
                    image=characteristic['image'], damage=characteristic['damage'], improve_array=characteristic['improve_cost_array'], armor_piercing=True,
                    poison=characteristic['poison'], additional_money=characteristic['additional_money'], radius=characteristic['radius'], context=context)
            case 5:
                buy_tower(
                    image=characteristic['image'], damage=characteristic['damage'], improve_array=characteristic['improve_cost_array'], armor_piercing=characteristic['armor_piercing'],
                    poison=characteristic['poison'] + 1, additional_money=characteristic['additional_money'], radius=characteristic['radius'], context=context)
            case 6:
                buy_tower(
                    image=characteristic['image'], damage=characteristic['damage'], improve_array=characteristic['improve_cost_array'], armor_piercing=characteristic['armor_piercing'],
                    poison=characteristic['poison'], additional_money=characteristic['additional_money'] + 2, radius=characteristic['radius'], context=context)
        context.config_gameplay.set_money(-characteristic['cost']*price_coefficient)

    def update(self, event, context, highlighting):
        if event:
            match event.name:
                case 'exit':
                    exit()
                case 'change_scene':
                    context.config_parameter_scene.set_scene(event.parameter['scene'])
                    if event.parameter['scene'].isdigit():
                        context.maps_array_iterator.change_level(event.parameter['scene'])
                        highlighting.update_scale(context)
                        context.config_constant_object.get_information_table().reset_modifier()
                        context.config_modifier.reset_price_modifier()
                        context.towers_array_iterator.update_scale_animation(context)
                        context.maps_array_iterator.update_trajectory_array()
                        context.maps_array_iterator.create_waves(100, context)  # создает волны
                        context.config_gameplay.set_current_wave(1 - context.config_gameplay.get_current_wave())  # текущая волна
                        context.enemies_array_iterator.create_enemy(context)  # создает врагов на 1 клетке
                        context.config_gameplay.set_is_started(False)  # переменная отвечает за то, началась ли игра или нет
                        context.config_gameplay.set_money(-context.config_gameplay.get_money() + 4)
                        for i in range(len(context.maps_array_iterator.get_build_array())):  # обнуляет все тайлы
                            context.maps_array_iterator.get_build_array()[i]['is_filled'] = False
                    context.buttons_groups_controller.change_buttons_active(context)
                case 'buy_tower':
                    is_free = context.config_modifier.get_is_free
                    price_up = context.config_modifier.get_price_up
                    if not price_up and not is_free and context.config_gameplay.get_money()>= json.loads(self.__products)[event.parameter['type']]['cost']:
                        self.__create_tower(1, context, event.parameter['type'])
                        context.maps_array_iterator.get_build_array()[context.config_gameplay.get_current_tile()]['is_filled'] = True
                    elif price_up and not is_free and context.config_gameplay.get_money()>= json.loads(self.__products)[event.parameter['type']]['cost'] * 2:
                        self.__create_tower(2, context, event.parameter['type'])
                        context.config_modifier.get_new_value_price_up(False)
                        context.maps_array_iterator.get_build_array()[context.config_gameplay.get_current_tile()]['is_filled'] = True
                    elif is_free:
                        self.__create_tower(0, context, event.parameter['type'])
                        context.config_modifier.get_new_value_price_up(False)
                        context.config_modifier.get_new_value_is_free(False)
                        context.maps_array_iterator.get_build_array()[context.config_gameplay.get_current_tile()]['is_filled'] = True
                case 'upgrade':
                    if context.towers_array_iterator.get_current_tower()and context.towers_array_iterator.get_current_tower().get_level() != 3:
                        cost = context.towers_array_iterator.get_current_tower().get_improve_cost_array()[context.towers_array_iterator.get_current_tower().get_level() - 1]
                        is_free = context.config_modifier.get_is_free
                        price_up = context.config_modifier.get_price_up
                        if is_free:
                            context.towers_array_iterator.get_current_tower().upgrade(1, 60)
                            context.towers_array_iterator.get_current_tower().set_level()
                            context.config_modifier.get_new_value_is_free(False)
                            context.config_modifier.get_new_value_price_up(False)
                            context.towers_array_iterator.append_upgrade(context)
                        elif price_up and context.config_gameplay.get_money()>= cost * 2:
                            context.towers_array_iterator.get_current_tower().upgrade(1, 60)
                            context.towers_array_iterator.get_current_tower().set_level()
                            context.config_gameplay.set_money(-cost * 2)
                            context.config_modifier.get_new_value_price_up(False)
                            context.towers_array_iterator.append_upgrade(context)
                        elif not price_up and context.config_gameplay.get_money()>= cost:
                            context.towers_array_iterator.get_current_tower().upgrade(1, 60)
                            context.towers_array_iterator.get_current_tower().set_level()
                            context.config_gameplay.set_money(-cost)
                            context.towers_array_iterator.append_upgrade(context)
                case 'sound_setting':
                    context.sound_controller.sound_setting(context)
                    context.buttons_groups_controller.update_state(context)
                case 'music_setting':
                    context.sound_controller.music_setting(context)
                    context.buttons_groups_controller.update_state(context)
                case 'using_additional_parameter_setting':
                    context.file_save_controller.change_true_false('always use additional parameter')
                    context.config_gameplay.set_always_use_additional_parameters(context.file_save_controller.get_parameter('always use additional parameter'))
                    context.buttons_groups_controller.update_state(context)