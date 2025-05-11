import abc
from scripts.classes_objects.bullet_class import Bullet, BulletWithAnimation

class AbstractStateDamage(abc.ABC):
    def __init__(self, func_array, damage_dict):
        self.__damage_dict = damage_dict
        self.__func_array = func_array

    def __composition_push_functions(self, enemy, functions, dict_arguments):
        if len(functions) == 1:
            return functions[0](enemy, dict_arguments)
        return functions[0](enemy, self.__composition_push_functions(enemy, functions.pop(0), dict_arguments), dict_arguments)

    def push(self, enemy):
        self.__composition_push_functions(enemy, self.__func_array, self.__damage_dict)

    @abc.abstractmethod
    def get_bullet(self, context, started_coordinate_center, final_coordinate_center):
        pass

class StateDamage(AbstractStateDamage):
    def __init__(self, func_array, image, damage_dict):
        super().__init__(func_array, damage_dict)
        self.__image = image

    def get_bullet(self, context, started_coordinate_center, final_coordinate_center):
        return Bullet(self.__image, started_coordinate_center, final_coordinate_center, context.animation_controller.get_fps(), context.maps_array_controller.get_tile_scale() * 0.2)

class StateDamageWithAnimatedBullet:
    def __init__(self, func_array, image_directory, damage_dict):
        super().__init__(func_array, damage_dict)
        self.__image_directory = image_directory

    def get_bullet(self, context, started_coordinate_center, final_coordinate_center):
        return BulletWithAnimation(self.__image_directory, started_coordinate_center, final_coordinate_center, context.animation_controller.get_fps(), context.maps_array_controller.get_tile_scale() * 0.2)