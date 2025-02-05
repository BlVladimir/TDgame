
import pygame
import sys

import EnemyClass
import MainManu
import Map
import Shop
import DefinitionCurrentTile
import LVL1
import Function
from Configs import ConfigParameterScreenClass, ConfigButtonClass, ConfigMapClass
import ContextClass

from ButtonClass import Button
from EnemyClass import Enemy, create_waves  # импорт классов из других файлов(чтобы уменьшить основной код)
from InformationClass import Information

pygame.init()  # импорт библиотеки pygame и sys, и импорт класса ClassButton из файла Button

clock = pygame.time.Clock()

scene = 'mainMenu'


def actionScene(lvl):  # функция, меняющая переменную сцены
    global scene
    scene = lvl

config_parameter_screen = ConfigParameterScreenClass.ConfigParameterScreen(1500, 1000)
config_button_screen = ConfigButtonClass.ConfigButton(config_parameter_screen.get_width(), config_parameter_screen.get_height(), actionScene)
config_map = ConfigMapClass.ConfigMap(config_parameter_screen.get_width(), config_parameter_screen.get_height())
context = ContextClass.Context(config_button_screen, config_map, config_parameter_screen)

use_additional_parameters = False
is_move = False
ti = 0
screen = pygame.display.set_mode((config_parameter_screen.get_width(), config_parameter_screen.get_height()))  # задает размер экрана и создает его
trajectory = ()
money = 3
current_tile = None
mouse_pose = [0, 0]
highlight_tile = None
amount_of_money = 'x 0'
amount_of_money_pos = (600, 70)
money_picture = pygame.transform.scale(pygame.image.load('images/UI/money.png'), (100, 100))
enemy_array = []
waves = []
current_wave = 0
current_enemy = None
current_tower = None
is_started = False
attacked_enemies = []
shop_tipe = 0
information_table = Information(config_parameter_screen.get_height(), config_parameter_screen.get_width())

always_use_additional_parameters = Function.find_in_file('alwaysUseAdditionalParameter')


def action_exit():  # функция, закрывающая окно
    pygame.quit()
    sys.exit()

def change_using_additional_parameter(additionalParameters):
    if additionalParameters:
        additionalParameters = False
    else:
        additionalParameters = True
    return additionalParameters

button_exit = Button(config_parameter_screen.get_width() - 170 - config_parameter_screen.get_height() * 0.4, 20, "images/UI/exit.png", 150, 75, action_exit)
button_main_manu = Button(150, 20, "images/UI/exitInMainManu.png", 100, 100, actionScene)
button_setting = Button(20, 20, "images/UI/settings.png", 100, 100, actionScene)  # объекты кнопок
button_additional_parameter = Button(config_parameter_screen.get_width() / 2, config_parameter_screen.get_height() / 2, 'images/UI/satingButtonTrue.png', 150, 150, change_using_additional_parameter)
enemy = Enemy("images/enemy/common.png", config_map.get_map_array()[0].get_started_position(4), config_map.get_map_array()[0].tile_scale / 2, 3)
highlight_tile_images = pygame.transform.scale(pygame.image.load("images/UI/highlighting/highlightingTower.png"), (100, 100))

while True:  # основной цикл
    for event in pygame.event.get():  # цикл получает значение event, и в зависимости от его типа делает определенное действие
        if event.type == pygame.QUIT:  # закрывает окно
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # если кнопка была нажата
            if scene == 'lvl1' and event.key == pygame.K_RETURN:  # эта кнопка Enter
                is_move = True  # переменная isMove нужна, чтобы определять, закончено движение или нет
        if pygame.key.get_pressed()[pygame.K_TAB]:  # была нажата кнопка таб
            use_additional_parameters = True
        else:
            use_additional_parameters = False
        match scene:
            case 'mainMenu':
                is_started = MainManu.handle_event(event, context)  # переменная, равняющаяся True только если кнопка перехода ан 1 уровень нажата
                if waves != [] or enemy_array != []:  # обнуляет массив врагов и их количество на каждой волне в меню
                    waves = []
                    enemy_array = []
                    Shop.towers_object_array = []
                    Shop.button_update_array = []
                if button_setting.is_pressed(event):
                    button_setting.handle_event_parameter('setting')
            case 'lvl1':
                if is_started:  # если кнопка перехода на 1 уровень нажата, то задает рандомно количество врагов от 1 до 3 на 10 волн
                    waves = create_waves(100, 3) #  создает волны
                    current_wave = 1  # текущая волна 1
                    EnemyClass.create_enemy_on_lvl1(waves, 0, enemy_array, context)  # создает врагов на 1 клетке
                    is_started = False  # переменная отвечает за то, началась ли игра или нет
                    money = 300
                    for i in range(len(config_map.get_map_array()[0].build_array)):  # обнуляет все тайлы
                        config_map.get_map_array()[0].build_array[i]['is_filled'] = False
                if Shop.towers_object_array is not []:
                    current_tower = Function.define_current_tower(current_tile, Shop.towers_object_array)
                if event.type == pygame.MOUSEBUTTONDOWN:  # если кнопка мыши нажата
                    current_enemy = DefinitionCurrentTile.highlight_enemy(enemy_array)  # определяет, какой враг выделен
                    if current_enemy is not None and Shop.towers_object_array != []:  # если выделенный враг существует и существует хотя бы одна башня
                        for i in range(len(Shop.towers_object_array)):  # проходится по всему массиву башен
                            if Shop.towers_object_array[i].index == current_tile and Shop.towers_object_array[i].is_in_radius(enemy_array[current_enemy].get_center()):  # если индекс башни равен текущему тайлу и текущий враг в радиусе башни
                                enemy_array[current_enemy].remove_health(Shop.towers_object_array[i].damage, Shop.towers_object_array[i].armor_piercing, Shop.towers_object_array[i].poison)  # отнимает у врага здоровье, равное урону башни
                                Shop.towers_object_array[i].is_used = True  # переменная отвечает за то, что башня была использована
                                if enemy_array[current_enemy].health <= 0:  # проверяет, упало ли здоровье врага ниже 0
                                    enemy_array.pop(current_enemy)  # если да, то удаляет его и прибавляет деньги
                                    current_enemy = None
                                    money, Function.is_free, Function.price_up, Function.type_new_modifier, Function.influence  = Function.bugs(Shop.towers_object_array, enemy_array, money, Function.is_free, Function.price_up)
                                    money += 2
                                break  # такая башня только одна, поэтому если такое случилось, то прерывает цикл
                if current_tile is not None and not config_map.get_map_array()[0].build_array[current_tile]['is_filled']:
                    shop_tipe = 1
                elif current_tile is not None and config_map.get_map_array()[0].build_array[current_tile]['is_filled']:
                    shop_tipe = 2
                else:
                    shop_tipe = 0
                if shop_tipe == 1:
                    money, config_map.get_map_array()[0].build_array, Shop.towers_object_array, Shop.button_update_array, Function.is_free, Function.price_up = Shop.build_tower(event, money, 100, current_tile, config_map.get_map_array()[0].build_array, Function.is_free, Function.price_up, context)  # если мышка нажмет на иконку башни в магазине, то башня построится на текущем тайле
                current_tile, highlight_tile = DefinitionCurrentTile.definition(event, config_map.get_map_array()[0].build_array, 100, current_tile, context)  # определяет текущий тайл
                for i in range(len(Shop.towers_object_array)):  # проходит по всему массиву башен, и если индекс башни совпадает с текущим тайлом, то вращает башню
                    if Shop.towers_object_array[i].index == current_tile and Shop.towers_object_array[i].image_gun is not None:
                        Shop.towers_object_array[i].rotate_gun()
                        Shop.towers_object_array[i].draw_radius(screen)
                if current_tower is not None and Shop.button_update_array[current_tower].is_pressed(event):
                    money, Function.is_free, Function.price_up = Shop.button_update_array[current_tower].handle_event_parameter({'tower_array': Shop.towers_object_array, 'number':current_tower, 'money':money, 'button_array':Shop.button_update_array, 'is_free':Function.is_free, 'price_up':Function.price_up})
                amount_of_money = 'x' + str(money) #  рисует количество денег
                if button_setting.is_pressed(event):
                    button_setting.handle_event_parameter('setting')
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')  # кнопка перехода в главное меню нажата
            case 'lvl2':
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')
            case 'lvl3':
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')
            case 'lvl4':
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')
            case 'lvl5':
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')
            case 'lvl6':
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')
            case 'setting':
                if button_additional_parameter.is_pressed(event):
                    always_use_additional_parameters = Function.file_change('alwaysUseAdditionalParameter')
                if button_main_manu.is_pressed(event):
                    button_main_manu.handle_event_parameter('mainMenu')
        button_exit.handle_event(event)
    if is_move:  # если движение не законченно, то враг двигается и идет проверка, закончено движение или нет
        is_fail = EnemyClass.move_all_enemies(enemy_array, trajectory, config_map.get_map_array()[0].gaps, config_map.get_map_array()[0].tile_scale)
        if is_fail:
            scene = 'mainMenu'
        ti += 1
        for i in range(len(Shop.towers_object_array)):
            Shop.towers_object_array[i].is_used = True
        if ti % 60 == 0:
            ti = 0
            is_move = False
            remove_array = []
            for i in range(len(enemy_array)):
                enemy_array[i].treat()
                if enemy_array[i].health <= 0:  # проверяет, упало ли здоровье врага ниже 0
                    remove_array.append(i)
            for i in range(len(remove_array)):
                enemy_array.pop(i)  # если да, то удаляет его и прибавляет деньги
                current_enemy = None
                money, Function.is_free, Function.price_up, Function.type_new_modifier, Function.influence = Function.bugs(Shop.towers_object_array, enemy_array, money, Function.is_free,Function.price_up)
                money += 2

            for i in range(len(Shop.towers_object_array)):
                Shop.towers_object_array[i].is_used = False  # После окончания движения врагов разрешает пользоваться башнями. Можно добавить модификатор нескольких использований башен или при максимальном уровне
            if current_wave != len(waves) and waves != []:  # после окончания движения создает врага на освободившейся клетке, если количество волн не дошло до конечной волны
                EnemyClass.create_enemy_on_lvl1(waves, current_wave, enemy_array, context)
                current_wave  += 1
    screen.fill((0, 0, 0))  # закрашивает весь экран, чтобы не было видно предыдущую сцену
    trajectory = config_map.get_map_array()[0].get_trajectory()
    match scene:  # То же, что и switch в других языках программирования. В зависимости от значения scene выполняет определенные действия. В данном случае используется для отрисовки определенных объектов
        case 'mainMenu':
            MainManu.draw_buttons(screen, context)
            button_setting.draw(screen)
        case 'lvl1':
            LVL1.draw_lvl1(screen, button_main_manu, button_setting, money_picture, enemy_array, current_enemy, highlight_tile_images, highlight_tile, current_tile, amount_of_money, amount_of_money_pos, use_additional_parameters, always_use_additional_parameters, shop_tipe, information_table, context)
        case 'lvl2':
            config_map.get_map_array()[1].draw(screen)
            button_main_manu.draw(screen)
            button_setting.draw(screen)
        case 'lvl3':
            config_map.get_map_array()[2].draw(screen)
            button_main_manu.draw(screen)
            button_setting.draw(screen)
        case 'lvl4':
            config_map.get_map_array()[3].draw(screen)
            button_main_manu.draw(screen)
            button_setting.draw(screen)
        case 'lvl5':
            config_map.get_map_array()[4].draw(screen)
            button_main_manu.draw(screen)
            button_setting.draw(screen)
        case 'lvl6':
            config_map.get_map_array()[5].draw(screen)
            button_main_manu.draw(screen)
            button_setting.draw(screen)
        case 'setting':
            button_additional_parameter.draw(screen)
            button_main_manu.draw(screen)
            button_exit.draw(screen)
    button_exit.draw(screen)  # вне switch, что бы всегда было видно
    pygame.display.flip()  # обновляет экран по завершению цикла
    clock.tick(60)  # ограничивает число кадров в секунду
