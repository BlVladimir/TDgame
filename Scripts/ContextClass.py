class Context:

    def __init__(self, config_constant_object, config_gameplay, config_modifier, config_parameter_scene, animation_controller, enemies_controller, towers_controller, maps_controller, file_save_controller, sound_controller):
        self.config_constant_object = config_constant_object
        self.config_gameplay = config_gameplay
        self.config_modifier = config_modifier
        self.config_parameter_scene = config_parameter_scene
        self.animation_controller = animation_controller
        self.enemies_controller = enemies_controller
        self.towers_controller = towers_controller
        self.maps_controller = maps_controller
        self.file_save_controller = file_save_controller
        self.sound_controller = sound_controller

    def get_config_constant_object(self):
        return self.config_constant_object

    def get_config_gameplay(self):
        return self.config_gameplay

    def get_config_modifier(self):
        return self.config_modifier

    def get_config_parameter_scene(self):
        return self.config_parameter_scene

    def get_animation_controller(self):
        return self.animation_controller

    def get_enemies_controller(self):
        return self.enemies_controller

    def get_towers_controller(self):
        return self.towers_controller

    def get_maps_controller(self):
        return self.maps_controller

    def get_file_save_controller(self):
        return self.file_save_controller

    def get_sound_controller(self):
        return self.sound_controller
