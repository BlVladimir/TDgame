class Context:

    def __init__(self, config_button, config_enemy, config_gameplay, config_map, config_modifier, config_parameter_scene, config_shop):
        self.config_button = config_button
        self.config_enemy = config_enemy
        self.config_gameplay = config_gameplay
        self.config_map = config_map
        self.config_modifier = config_modifier
        self.config_parameter_scene = config_parameter_scene
        self.config_shop = config_shop

    def get_config_button(self):
        return self.config_button

    def get_config_enemy(self):
        return self.config_enemy

    def get_config_gameplay(self):
        return self.config_gameplay

    def get_config_map(self):
        return self.config_map

    def get_config_modifier(self):
        return self.config_modifier

    def get_config_parameter_scene(self):
        return self.config_parameter_scene

    def get_config_shop(self):
        return self.config_shop
