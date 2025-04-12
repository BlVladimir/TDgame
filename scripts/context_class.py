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

    @property
    def config_constant_object(self):
        return self.__config_constant_object

    @property
    def config_gameplay(self):
        return self.__config_gameplay

    @property
    def config_modifier(self):
        return self.__config_modifier

    @property
    def config_parameter_scene(self):
        return self.__config_parameter_scene

    @property
    def animation_controller(self):
        return self.__animation_controller

    @property
    def enemies_controller(self):
        return self.__enemies_controller

    @property
    def towers_controller(self):
        return self.__towers_controller

    @property
    def maps_controller(self):
        return self.__maps_controller

    @property
    def file_save_controller(self):
        return self.__file_save_controller

    @property
    def sound_controller(self):
        return self.__sound_controller

    @property
    def settings_objects(self):
        return self.__settings_objects