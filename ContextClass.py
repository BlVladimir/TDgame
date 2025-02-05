class Context:

    def __init__(self, config_parameter_scene, config_button):
        self.config_parameter_scene = config_parameter_scene
        self.config_button = config_button

    def get_config_parameter_scene(self):
        return self.config_parameter_scene

    def get_config_button(self):
        return self.config_button