import os
import pygame
from Scripts.MainScripts.Function import draw_text

class AnimationController:
    def __init__(self, config_parameter_screen):
        self.__is_move = False
        self.__time_move = 0
        self.__time_game_over = 0
        self.__is_fail = False
        self.__animation_game_over = []
        files_animation_game_over = os.listdir('images/UI/gameOverAnimation')
        for i in files_animation_game_over:
            self.__animation_game_over.append(pygame.transform.scale(pygame.image.load('images/UI/gameOverAnimation/' + i), (config_parameter_screen.get_width(), config_parameter_screen.get_height())))

    def start_move(self):
        self.__is_move = True

    def move_enemies(self, context):
        if self.__is_move:  # если движение не законченно, то враг двигается и идет проверка, закончено движение или нет
            self.__time_move += 1
            context.get_towers_controller().turn_off_or_on_all_towers(True)
            context.get_enemies_controller().move_all_enemies(100, self.__time_move, context, 120)
            if self.__time_move % 120 == 0:
                context.get_enemies_controller().stop_walk()
                self.__time_move = 0
                self.__is_move = False
                context.get_enemies_controller().treat_enemies(context)
                context.get_towers_controller().turn_off_or_on_all_towers(False)  # После окончания движения врагов разрешает пользоваться башнями. Можно добавить модификатор нескольких использований башен или при максимальном уровне
                if context.get_config_gameplay().get_current_wave() != len(context.get_config_gameplay().get_waves()) and context.get_config_gameplay().get_waves() != []:  # после окончания движения создает врага на освободившейся клетке, если количество волн не дошло до конечной волны
                    context.get_enemies_controller().create_enemy(context)
                    context.get_config_gameplay().set_current_wave(1)

    def fail_animation(self, context):
        if self.__time_game_over < 30:
            self.__time_game_over += 1
        elif 30 <= self.__time_game_over < 60:
            context.get_config_parameter_scene().get_screen().blit(self.__animation_game_over[(self.__time_game_over - 30)//2], (0, 0))
            self.__time_game_over += 1
        elif 60 <= self.__time_game_over < 180:
            context.get_config_parameter_scene().get_screen().blit(self.__animation_game_over[14], (0, 0))
            if (self.__time_game_over // 20) % 2 == 0:
                draw_text('game over', 100, (200, 30), context)
            else:
                draw_text('game over_', 100, (200, 30), context)
            self.__time_game_over += 1
        else:
            self.__time_game_over = 0
            context.get_config_gameplay().set_is_fail(False)
            context.get_config_parameter_scene().set_scene('mainMenu')

    def get_time_game_over(self):
        return self.__time_game_over
