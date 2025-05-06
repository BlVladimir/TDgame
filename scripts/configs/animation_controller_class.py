import os
import pygame
from scripts.main_scripts.function import draw_text
from scripts.main_scripts.resourse_path import resource_path
from scripts.classes_objects.event_class import ButtonEvent

class AnimationController:
    def __init__(self, config_parameter_screen):
        self.__is_move = False  # двигаются ли враги
        self.__time_move = 0  # время движения
        self.__time_game_over = 0  # время анимации пройгрыша
        self.__is_fail = False  # проиграл игрок или нет
        self.__animation_game_over = []
        files_animation_game_over = os.listdir(resource_path('images/UI/game_over_animation'))  # получает все файлы по данному пути
        for i in files_animation_game_over:
            self.__animation_game_over.append(pygame.transform.scale(pygame.image.load(resource_path('images/UI/game_over_animation/' + i)), (config_parameter_screen.get_width(), config_parameter_screen.get_height())))  # загружает все картинки анимации пройгрыша
        self.__fps = 30  # кадры в секунду

    def start_move(self, context):  # враги начинают двигаться
        self.__is_move = True
        context.sound_controller.play_sound('walk')

    def move_enemies(self, context):  # движение всех врагов
        if self.__is_move:  # если движение не законченно, то враг двигается и идет проверка, закончено движение или нет
            self.__time_move += 1
            context.towers_controller.turn_off_or_on_all_towers(True)
            context.enemies_controller.move_all_enemies(self.__time_move, context, 60)
            if self.__time_move % 60 == 0:
                context.enemies_controller.stop_walk(context)
                self.__time_move = 0
                self.__is_move = False
                context.enemies_controller.treat_enemies(context)
                context.towers_controller.turn_off_or_on_all_towers(False)  # После окончания движения врагов разрешает пользоваться башнями. Можно добавить модификатор нескольких использований башен или при максимальном уровне
                if context.config_gameplay.get_current_wave()!= len(context.config_gameplay.get_waves()) and context.config_gameplay.get_waves()!= []:  # после окончания движения создает врага на освободившейся клетке, если количество волн не дошло до конечной волны
                    context.enemies_controller.create_enemy(context)
                    context.config_gameplay.set_current_wave(1)

    def fail_animation(self, context, highlighting):  # Анимация при пройгрыше. Кнопка exit работает, но ее не видно
        if self.__time_game_over < 30:
            self.__time_game_over += 1
        elif 30 <= self.__time_game_over < 60:
            context.config_parameter_scene.get_screen().blit(self.__animation_game_over[(self.__time_game_over - 30) // 2], (0, 0))
            self.__time_game_over += 1
        elif 60 <= self.__time_game_over < 180:
            context.config_parameter_scene.get_screen().blit(self.__animation_game_over[14], (0, 0))
            if (self.__time_game_over // 20) % 2 == 0:
                draw_text('game over', 70, (30, 30), context, 1)
            else:
                draw_text('game over_', 70, (30, 30), context, 1)
            self.__time_game_over += 1
        else:
            self.__time_game_over = 0
            context.config_gameplay.set_is_fail(False)
            context.event_controller.update(ButtonEvent('change_scene', scene='main_menu'), context, highlighting)

    def get_time_game_over(self):
        return self.__time_game_over

    def get_fps(self):
        return self.__fps
