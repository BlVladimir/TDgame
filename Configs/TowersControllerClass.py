import os
import pygame

class TowerController:

    def __init__(self, scale):
        self.__towers_object_array = []
        self.__button_update_array = []
        self.__animation_upgrade = []
        self.__upgrade_array = []
        files_animation = os.listdir('images/upgrade/animationUpgrade')
        for i in files_animation:
            self.__animation_upgrade.append(pygame.transform.scale(pygame.image.load('images/upgrade/animationUpgrade/' + i), (scale, scale)))
        self.__current_tower = None


    def get_current_button_update(self):
        if self.__button_update_array:
            return self.__button_update_array[self.__current_tower]

    def append_tower_object(self, new_tower_object, new_button_object):
        self.__towers_object_array.append(new_tower_object)
        self.__button_update_array.append(new_button_object)

    def clear_towers_arrays(self):
        self.__towers_object_array.clear()
        self.__button_update_array.clear()

    def turn_off_or_on_all_towers(self, state):
        for i in range(len(self.__towers_object_array)):
            self.__towers_object_array[i].is_used = state

    def get_current_tower(self):
        if self.__current_tower is not None:
            return self.__towers_object_array[self.__current_tower]

    def define_current_tower(self, context):  # определяет текущую башню по индексу
        self.__current_tower = None
        if self.__towers_object_array:
            for i in range(len(self.__towers_object_array)):
                if self.__towers_object_array[i].index == context.get_config_gameplay().get_current_tile():
                    self.__current_tower = i
                    break

    def change_damage(self, influence):
        if influence == 0:
            for i in range(len(self.__towers_object_array)):
                if self.__towers_object_array[i].damage > 1:
                    self.__towers_object_array[i].damage -= 1
        else:
            for i in range(len(self.__towers_object_array)):
                self.__towers_object_array[i].damage += 1

    def append_upgrade(self, context):
        self.__upgrade_array.append([context.get_maps_controller().get_build_array()[context.get_config_gameplay().get_current_tile()]['coordinate'], 0])

    def draw_animation_upgrade(self, context):
        if self.__upgrade_array:
            __delete_array = []
            for i in range(len(self.__upgrade_array)):
                context.get_config_parameter_scene().get_screen().blit(self.__animation_upgrade[self.__upgrade_array[i][1]], self.__upgrade_array[i][0])
                self.__upgrade_array[i][1] += 1
                if self.__upgrade_array[i][1] >= 30:
                    __delete_array.append(i)
            for i in range(len(__delete_array)):
                self.__upgrade_array.pop(__delete_array[len(__delete_array) - 1 - i])

    def draw_towers(self, context):
        if self.__towers_object_array:
            for i in self.__towers_object_array:  # проходится по массиву объектов башен и рисует их
                i.draw_tower(context)
            if self.__current_tower is not None and self.__towers_object_array[self.__current_tower].radius:
                self.__towers_object_array[self.__current_tower].draw_radius(context)