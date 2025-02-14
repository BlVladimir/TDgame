class Context:

    def __init__(self, config_constant_object, config_enemy, config_gameplay, config_map, config_modifier, config_parameter_scene):
        self.config_constant_object = config_constant_object
        self.config_enemy = config_enemy
        self.config_gameplay = config_gameplay
        self.config_map = config_map
        self.config_modifier = config_modifier
        self.config_parameter_scene = config_parameter_scene

    def get_config_constant_object(self):
        return self.config_constant_object

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
