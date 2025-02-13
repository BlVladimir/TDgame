from Function import find_in_file

class ConfigGameplay:

    def __init__(self, amount_of_money_position):
        self.amount_of_money = 'x 0'
        self.amount_of_money_position = amount_of_money_position
        self.current_tower = None
        self.highlight_tile = None
        self.current_tile = None
        self.shop_type = 0
        self.money = 0
        self.use_additional_parameters = False
        self.waves = []
        self.current_wave = 0
        self.is_started = False
        self.always_use_additional_parameters = find_in_file('alwaysUseAdditionalParameter')


    def get_current_tower(self):
        return self.current_tower

    def new_value_current_tower(self, new_value):
        self.current_tower = new_value

    def get_highlight_tile(self):
        return self.highlight_tile

    def new_value_highlight_tile(self, new_value):
        self.highlight_tile = new_value

    def get_current_tile(self):
        return self.current_tile

    def new_value_current_tile(self, new_value):
        self.current_tile = new_value

    def get_amount_of_money(self):
        return self.amount_of_money

    def new_value_amount_of_money(self, new_value):
        self.amount_of_money = new_value

    def get_amount_of_money_position(self):
        return self.amount_of_money_position

    def get_shop_type(self):
        return self.shop_type

    def new_value_shop_type(self, new_value):
        self.shop_type = new_value

    def get_money(self):
        return self.money

    def new_value_money(self, new_value):
        self.money = self.money + new_value

    def get_use_additional_parameters(self):
        return self.use_additional_parameters

    def new_value_use_additional_parameters(self, new_value):
        self.use_additional_parameters = new_value

    def get_waves(self):
        return self.waves

    def new_value_waves(self, new_value):
        self.waves = new_value

    def get_current_wave(self):
        return self.current_wave

    def new_value_current_wave(self, new_value):
        self.current_wave = self.current_wave + new_value

    def get_is_started(self):
        return self.is_started

    def new_value_is_started(self, new_value):
        self.is_started = new_value

    def get_always_use_additional_parameters(self):
        return self.always_use_additional_parameters

    def new_value_always_use_additional_parameters(self, new_value):
        self.always_use_additional_parameters = new_value