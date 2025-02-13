class ConfigEnemy:

    def __init__(self):
        self.current_enemy = None
        self.is_move = False
        self.time = 0
        self.trajectory = ()
        self.enemy_array = []

    def get_current_enemy(self):
        return self.current_enemy

    def new_value_current_enemy(self, new_value):
        self.current_enemy = new_value

    def get_is_move(self):
        return self.is_move

    def new_value_is_move(self, new_value):
        self.is_move = new_value

    def get_time(self):
        return self.time

    def new_value_time(self, new_value):
        self.time = self.time + new_value

    def get_trajectory(self):
        return self.trajectory

    def new_value_trajectory(self, new_value):
        self.trajectory = new_value

    def get_enemy_array(self):
        return self.enemy_array

    def new_value_enemy_array(self, new_value):
        self.enemy_array = new_value