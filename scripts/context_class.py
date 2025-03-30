class Context:

    def __init__(self, config_constant_object, config_gameplay, config_modifier, config_parameter_scene, animation_controller, enemies_controller, towers_controller, maps_controller, file_save_controller, sound_controller, settings_objects):
        self.__config_constant_object = config_constant_object
        self.__config_gameplay = config_gameplay
        self.__config_modifier = config_modifier
        self.__config_parameter_scene = config_parameter_scene
        self.__animation_controller = animation_controller
        self.__enemies_controller = enemies_controller
        self.__towers_controller = towers_controller
        self.__maps_controller = maps_controller
        self.__file_save_controller = file_save_controller
        self.__sound_controller = sound_controller
        self.__settings_objects = settings_objects

    def get_config_constant_object(self):
        return self.__config_constant_object

    def get_config_gameplay(self):
        return self.__config_gameplay

    def get_config_modifier(self):
        return self.__config_modifier

    def get_config_parameter_scene(self):
        return self.__config_parameter_scene

    def get_animation_controller(self):
        return self.__animation_controller

    def get_enemies_controller(self):
        return self.__enemies_controller

    def get_towers_controller(self):
        return self.__towers_controller

    def get_maps_controller(self):
        return self.__maps_controller

    def get_file_save_controller(self):
        return self.__file_save_controller

    def get_sound_controller(self):
        return self.__sound_controller

    def get_settings_objects(self):
        return self.__settings_objects