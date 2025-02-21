class AnimationController:
    def __init__(self):
        self.__is_move = False
        self.__time = 0
        self.__is_fail = False

    def get_is_move(self):
        return self.__is_move

    def new_value_is_move(self, new_value):
        self.__is_move = new_value

    def get_time(self):
        return self.__time

    def new_value_time(self, new_value):
        self.__time = self.__time + new_value

    def start_move(self):
        self.__is_move = True

    def move_enemies(self, enemies_controller, towers_controller, maps_controller, context):
        if self.__is_move:  # если движение не законченно, то враг двигается и идет проверка, закончено движение или нет
            self.__time += 1
            towers_controller.turn_off_or_on_all_towers(True)
            enemies_controller.move_all_enemies(100, self.__time, maps_controller, context)
            if self.__time % 60 == 0:
                self.__time = 0
                self.__is_move = False
                enemies_controller.treat_enemies(enemies_controller, towers_controller, context)
                towers_controller.turn_off_or_on_all_towers(False)  # После окончания движения врагов разрешает пользоваться башнями. Можно добавить модификатор нескольких использований башен или при максимальном уровне
                if context.get_config_gameplay().get_current_wave() != len(context.get_config_gameplay().get_waves()) and context.get_config_gameplay().get_waves() != []:  # после окончания движения создает врага на освободившейся клетке, если количество волн не дошло до конечной волны
                    enemies_controller.create_enemy(context, maps_controller, 1)
                    context.get_config_gameplay().new_value_current_wave(1)