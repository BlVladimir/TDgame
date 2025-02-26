from Scripts.MainScripts.Function import find_in_file

class ConfigGameplay:

    def __init__(self, amount_of_money_position):
        self.__amount_of_money = 'x 0'
        self.__amount_of_money_position = amount_of_money_position
        self.__current_tower = None
        self.__highlight_tile = None
        self.__current_tile = None
        self.__shop_type = 0
        self.__money = 0
        self.__use_additional_parameters = False
        self.__waves = []
        self.__current_wave = 0
        self.__is_started = False
        self.__always_use_additional_parameters = find_in_file('alwaysUseAdditionalParameter')
        self.__is_fail = False

    def get_highlight_tile(self):
        return self.__highlight_tile

    def set_highlight_tile(self, new_value):
        self.__highlight_tile = new_value

    def get_current_tile(self):
        return self.__current_tile

    def set_current_tile(self, new_value):
        self.__current_tile = new_value

    def get_amount_of_money(self):
        return self.__amount_of_money

    def set_amount_of_money(self, new_value):
        self.__amount_of_money = new_value

    def get_amount_of_money_position(self):
        return self.__amount_of_money_position

    def get_shop_type(self):
        return self.__shop_type

    def set_shop_type(self, new_value):
        self.__shop_type = new_value

    def get_money(self):
        return self.__money

    def set_money(self, new_value):
        self.__money = self.__money + new_value

    def get_use_additional_parameters(self):
        return self.__use_additional_parameters

    def set_use_additional_parameters(self, new_value):
        self.__use_additional_parameters = new_value

    def get_waves(self):
        return self.__waves

    def set_waves(self, new_value):
        self.__waves = new_value

    def get_current_wave(self):
        return self.__current_wave

    def set_current_wave(self, new_value):
        self.__current_wave = self.__current_wave + new_value

    def get_is_started(self):
        return self.__is_started

    def set_is_started(self, new_value):
        self.__is_started = new_value

    def get_always_use_additional_parameters(self):
        return self.__always_use_additional_parameters

    def set_always_use_additional_parameters(self, new_value):
        self.__always_use_additional_parameters = new_value

    def get_is_fail(self):
        return self.__is_fail

    def set_is_fail(self, new_value):
        self.__is_fail = new_value
