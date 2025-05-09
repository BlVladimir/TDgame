from scripts.classes_objects.bullet_class import Bullet, BulletWithAnimation

class StateDamage:
    def __init__(self, func_array, image):
        self.__func_array = func_array
        self.__image = image

    def __composition_push_functions(self, enemy, functions, dict_arguments):
        if len(functions) == 1:
            return functions[0](enemy, dict_arguments)
        return functions[0](enemy, self.__composition_push_functions, dict_arguments)

    def push(self, enemy, **kwargs):
        self.__composition_push_functions(enemy, self.__func_array, kwargs)

    def get_bullet(self, context, started_coordinate_center, final_coordinate_center):
        return Bullet(self.__image, started_coordinate_center, final_coordinate_center, context.animation_controller.get_fps(), context.maps_array_controller.get_tile_scale() * 0.2)

class StateDamageWithAnimatedBullet:
    def __init__(self, func_array, image_directory):
        self.__func_array = func_array
        self.__image_directory = image_directory

    def __composition_push_functions(self, enemy, functions, dict_arguments):
        if len(functions) == 1:
            return functions[0](enemy, dict_arguments)
        return functions[0](enemy, self.__composition_push_functions, dict_arguments)

    def push(self, enemy, **kwargs):
        self.__composition_push_functions(enemy, self.__func_array, kwargs)

    def get_bullet(self, context, started_coordinate_center, final_coordinate_center):
        return Bullet(self.__image_directory, started_coordinate_center, final_coordinate_center, context.animation_controller.get_fps(), context.maps_array_controller.get_tile_scale() * 0.2)