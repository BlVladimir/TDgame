class Context:

    def __init__(self, config_button, config_map, config_parameter_scene):
        self.config_button = config_button
        self.config_map = config_map
        self.config_parameter_scene = config_parameter_scene

    def get_config_button(self):
        return self.config_button

    def get_config_map(self):
        return self.config_map

    def get_config_parameter_scene(self):
        return self.config_parameter_scene