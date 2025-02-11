class ConfigGameplay:

    def __init__(self, amount_of_money_position):
        self.amount_of_money = 'x 0'
        self.amount_of_money_position = amount_of_money_position
        self.current_enemy = None
        self.current_tower = None
        self.highlight_tile = None
        self.current_tile = None
        self.is_move = False
        self.time = 0
        self.shop_tipe = 0
        self.money = 3
        self.trajectory = ()
        self.enemy_array = []

    def get_current_enemy(self):
        return self.current_enemy

    def new_value_current_enemy(self, new_value):
        self.current_enemy = new_value

    def get_current_tower(self):
        return self.current_tower

    def new_value_current_tower(self, new_value):
        self.current_tower = new_value

    def get_highlight_tile(self):
        return self.highlight_tile

    def new_highlight_tile(self, new_value):
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

    def get_is_move(self):
        return self.is_move

    def new_value_is_move(self, new_value):
        self.is_move = new_value

    def get_time(self):
        return self.time

    def new_value_time(self, new_value):
        self.time = new_value

    def get_shop_tipe(self):
        return self.shop_tipe

    def new_value_shop_tipe(self, new_value):
        self.shop_tipe = new_value

    def get_money(self):
        return self.money

    def new_value_money(self, new_value):
        self.money = new_value

    def get_trajectory(self):
        return self.trajectory

    def new_value_trajectory(self, new_value):
        self.trajectory = new_value

    def get_enemy_array(self):
        return self.current_enemy

    def new_value_enemy_array(self, new_value):
        self.current_enemy = new_value