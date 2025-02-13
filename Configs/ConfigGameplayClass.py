class ConfigGameplay:

    def __init__(self, amount_of_money_position):
        self.amount_of_money = 'x 0'
        self.amount_of_money_position = amount_of_money_position
        self.current_tower = None
        self.highlight_tile = None
        self.current_tile = None
        self.shop_type = 0
        self.money = 0
        use_additional_parameters = False
        mouse_pose = [0, 0]
        waves = []
        current_wave = 0
        is_started = False
        always_use_additional_parameters = Function.find_in_file('alwaysUseAdditionalParameter')


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