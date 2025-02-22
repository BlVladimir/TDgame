

class AnimationController:
    def __init__(self):
        self.__is_move = False
        self.__time_move = 0
        self.__is_fail = False

    def start_move(self):
        self.__is_move = True

    def move_enemies(self, context):
        if self.__is_move:  # если движение не законченно, то враг двигается и идет проверка, закончено движение или нет
            self.__time_move += 1
            context.get_towers_controller().turn_off_or_on_all_towers(True)
            context.get_enemies_controller().move_all_enemies(100, self.__time_move, context)
            if self.__time_move % 60 == 0:
                self.__time_move = 0
                self.__is_move = False
                context.get_enemies_controller().treat_enemies(context)
                context.get_towers_controller().turn_off_or_on_all_towers(False)  # После окончания движения врагов разрешает пользоваться башнями. Можно добавить модификатор нескольких использований башен или при максимальном уровне
                if context.get_config_gameplay().get_current_wave() != len(context.get_config_gameplay().get_waves()) and context.get_config_gameplay().get_waves() != []:  # после окончания движения создает врага на освободившейся клетке, если количество волн не дошло до конечной волны
                    context.get_enemies_controller().create_enemy(context)
                    context.get_config_gameplay().new_value_current_wave(1)