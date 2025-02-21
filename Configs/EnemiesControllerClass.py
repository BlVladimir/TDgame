from random import randrange

import pygame
import EnemyClass
from Function import bugs


class EnemiesController:

    def __init__(self):
        self.__current_enemy = None
        self.__enemy_array = []

    def define_current_enemy(self):
        self.__current_enemy = None
        if self.__enemy_array:
            scale = self.__enemy_array[0].scale
            mousePose = pygame.mouse.get_pos()
            for i in range(len(self.__enemy_array)):
                if self.__enemy_array[i].rect[0] + scale * 0.9 >= mousePose[0] >= self.__enemy_array[i].rect[0] + scale * 0.1 and self.__enemy_array[i].rect[1] + scale * 0.9 >= mousePose[1] >= self.__enemy_array[i].rect[1] + scale * 0.1:
                    self.__current_enemy = i
                    break

    def get_current_enemy(self):
        if self.__current_enemy is not None:
            return self.__enemy_array[self.__current_enemy]
        else:
            return None

    def clear_enemies_array(self):
        self.__enemy_array.clear()

    def kill_enemies(self, enemies_controller, towers_controller, context):
        __kill_array = []
        for i in range(len(self.__enemy_array)):
            if self.__enemy_array[i].health <= 0:
                __kill_array.append(i)
        self.__current_enemy = None
        for i in range(len(__kill_array)):
            self.__enemy_array.pop(__kill_array[len(__kill_array)-1-i])
            bugs(enemies_controller, context, towers_controller)
            context.get_config_gameplay().new_value_money(2)

    def treat_enemies(self, enemies_controller, towers_controller, context):
        for i in range(len(self.__enemy_array)):
            self.__enemy_array[i].treat()
        self.kill_enemies(enemies_controller, towers_controller, context)

    def move_all_enemies(self, tile_scale, time, maps_controller, context, speed=60):  # двигает всех врагов
        for i in range(len(self.__enemy_array)):
            self.__enemy_array[i].move(tile_scale, time, maps_controller, context, speed)
            if context.get_config_gameplay().get_is_fail():
                break

    def change_health_enemy(self, influence):
        if influence == 1:
            for i in range(len(self.__enemy_array)):
                if self.__enemy_array[i].health > 1:
                    self.__enemy_array[i].health -= 1
        else:
            for i in range(len(self.__enemy_array)):
                self.__enemy_array[i].health += 1

    def draw_enemies(self, context):
        for i in range(len(self.__enemy_array)):  # рисует каждого врага
            self.__enemy_array[i].draw(context)

    def create_enemy(self, context, maps_controller, level):  # Добавляет в массив врагов новые элементы. В зависимости от количества врагов у каждого врага разные координаты
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
        scale = maps_controller.get_scale()
        if context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave()][0] == 1:
            self.__enemy_array.append(EnemyClass.Enemy(image_enemy, maps_controller.get_started_position(level, 0), scale / 2, health + additional_health, armor=armor, treatment=treatment))
        elif context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave()][0] == 2:
            self.__enemy_array.append(EnemyClass.Enemy(image_enemy, maps_controller.get_started_position(level, 1), scale / 2, health + additional_health, armor=armor, treatment=treatment))
            self.__enemy_array.append(EnemyClass.Enemy(image_enemy, maps_controller.get_started_position(level, 2), scale / 2, health + additional_health, armor=armor, treatment=treatment))
        elif context.get_config_gameplay().get_waves()[context.get_config_gameplay().get_current_wave()][0] == 3:
            self.__enemy_array.append(EnemyClass.Enemy(image_enemy, maps_controller.get_started_position(level, 2), scale / 2, health + additional_health, armor=armor, treatment=treatment))
            self.__enemy_array.append(EnemyClass.Enemy(image_enemy, maps_controller.get_started_position(level, 3), scale / 2, health + additional_health, armor=armor, treatment=treatment))
            self.__enemy_array.append(EnemyClass.Enemy(image_enemy, maps_controller.get_started_position(level, 4), scale / 2, health + additional_health, armor=armor, treatment=treatment))