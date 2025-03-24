from random import randrange

import pygame
from Scripts.ClassesObjects import EnemyClass
from Scripts.MainScripts.Function import bugs


class EnemiesController:

    def __init__(self):
        self.__current_enemy = None
        self.__enemy_array = []

    def define_current_enemy(self):
        self.__current_enemy = None
        if self.__enemy_array:
            scale = self.__enemy_array[0].get_scale()
            mousePose = pygame.mouse.get_pos()
            for i in range(len(self.__enemy_array)):
                if self.__enemy_array[i].get_rect()[0] + scale * 0.9 >= mousePose[0] >= self.__enemy_array[i].get_rect()[0] + scale * 0.1 and self.__enemy_array[i].get_rect()[1] + scale * 0.9 >= mousePose[1] >= self.__enemy_array[i].get_rect()[1] + scale * 0.1:
                    self.__current_enemy = i
                    break

    def get_current_enemy(self):
        if self.__current_enemy is not None:
            return self.__enemy_array[self.__current_enemy]
        else:
            return None

    def clear_enemies_array(self):
        self.__enemy_array.clear()

    def kill_enemies(self, context):
        __kill_array = []
        for i in range(len(self.__enemy_array)):
            if self.__enemy_array[i].get_health() <= 0:
                __kill_array.append(i)
        self.__current_enemy = None
        for i in range(len(__kill_array)):
            context.get_config_gameplay().set_money(2 + self.__enemy_array[__kill_array[len(__kill_array) - 1 - i]].get_additional_money())
            self.__enemy_array.pop(__kill_array[len(__kill_array)-1-i])
            bugs(context)

    def treat_enemies(self, context):
        for i in range(len(self.__enemy_array)):
            self.__enemy_array[i].treat()
        self.kill_enemies(context)

    def move_all_enemies(self, time, context, speed=60):  # двигает всех врагов
        for i in range(len(self.__enemy_array)):
            self.__enemy_array[i].move(time, context, speed)
            if context.get_config_gameplay().get_is_fail():
                if context.get_config_gameplay().get_current_wave() >= 20 and context.get_config_gameplay().get_passed_level(context) < context.get_maps_controller().get_level():
                    context.get_file_save_controller().set_parameter('level', context.get_maps_controller().get_level())
                    self.__current_enemy = None

                break

    def stop_walk(self):
        for i in range(len(self.__enemy_array)):
            self.__enemy_array[i].end_walk()

    def change_health_enemy(self, influence):
        if influence == 1:
            for i in range(len(self.__enemy_array)):
                if self.__enemy_array[i].get_health() > 1:
                    self.__enemy_array[i].set_health(-1)
        else:
            for i in range(len(self.__enemy_array)):
                self.__enemy_array[i].set_health(1)

    def draw_enemies(self, context):
        for i in range(len(self.__enemy_array)):  # рисует каждого врага
            self.__enemy_array[i].draw(context)

    def create_enemy(self, context):  # Добавляет в массив врагов новые элементы. В зависимости от количества врагов у каждого врага разные координаты
        if (context.get_config_gameplay().get_current_wave() + 1) % 4 == 0:
            additional_health = ((context.get_config_gameplay().get_current_wave() + 1) // 4 - 1) * 2 + 1
        else:
            additional_health = ((context.get_config_gameplay().get_current_wave() + 1) // 4) * 2 + (context.get_config_gameplay().get_current_wave() + 1) % 4 - 1
        additional_health += randrange(-1, 2)
        image_enemy = 'images/enemy/common.png'
        health = 3
        armor = 0
        treatment = 0
        match context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave() - 1][1]:
            case 1:
                image_enemy = 'images/enemy/armoredEnemy.png'
                health = 6
            case 2:
                image_enemy = 'images/enemy/ShieldEnemy.png'
                armor = 3
            case 3:
                image_enemy = 'images/enemy/regen.png'
                health = 4
                treatment = 2
        scale = context.get_maps_controller().get_tile_scale()
        angle = context.get_maps_controller().get_started_angle()
        if context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave()][0] == 1:
            self.__enemy_array.append(
                EnemyClass.Enemy(image_enemy, context.get_maps_controller().get_started_position(0), scale / 2, angle, health + additional_health, context.get_config_gameplay().get_current_wave() // 2, 0, armor=armor, treatment=treatment))
        elif context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave()][0] == 2:
            self.__enemy_array.append(
                EnemyClass.Enemy(image_enemy, context.get_maps_controller().get_started_position(1), scale / 2, angle, health + additional_health, context.get_config_gameplay().get_current_wave() // 2, 1, armor=armor, treatment=treatment))
            self.__enemy_array.append(
                EnemyClass.Enemy(image_enemy, context.get_maps_controller().get_started_position(2), scale / 2, angle, health + additional_health, context.get_config_gameplay().get_current_wave() // 2, 2, armor=armor, treatment=treatment))
        elif context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave()][0] == 3:
            self.__enemy_array.append(
                EnemyClass.Enemy(image_enemy, context.get_maps_controller().get_started_position(2), scale / 2, angle, health + additional_health, context.get_config_gameplay().get_current_wave() // 2, 2, armor=armor, treatment=treatment))
            self.__enemy_array.append(
                EnemyClass.Enemy(image_enemy, context.get_maps_controller().get_started_position(3), scale / 2, angle, health + additional_health, context.get_config_gameplay().get_current_wave() // 2, 3, armor=armor, treatment=treatment))
            self.__enemy_array.append(
                EnemyClass.Enemy(image_enemy, context.get_maps_controller().get_started_position(4), scale / 2, angle, health + additional_health, context.get_config_gameplay().get_current_wave() // 2, 4, armor=armor, treatment=treatment))