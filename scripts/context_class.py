class Context:
    def __init__(self, config_constant_object, config_gameplay, config_modifier, config_parameter_scene, animation_controller, enemies_array_iterator, towers_array_iterator, maps_array_iterator, file_save_controller, sound_controller, event_controller, buttons_groups_controller):
        self.__config_constant_object = config_constant_object
        self.__config_gameplay = config_gameplay
        self.__config_modifier = config_modifier
        self.__config_parameter_scene = config_parameter_scene
        self.__animation_controller = animation_controller
        self.__enemies_array_iterator = enemies_array_iterator
        self.__towers_array_iterator = towers_array_iterator
        self.__maps_array_iterator = maps_array_iterator
        self.__file_save_controller = file_save_controller
        self.__sound_controller = sound_controller
        self.__event_controller = event_controller
        self.__buttons_groups_controller = buttons_groups_controller

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
    def enemies_array_iterator(self):
        return self.__enemies_array_iterator

    @property
    def towers_array_iterator(self):
        return self.__towers_array_iterator

    @property
    def maps_array_iterator(self):
        return self.__maps_array_iterator

    @property
    def file_save_controller(self):
        return self.__file_save_controller

    @property
    def sound_controller(self):
        return self.__sound_controller

    @property
    def event_controller(self):
        return self.__event_controller

    @property
    def buttons_groups_controller(self):
        return self.__buttons_groups_controller