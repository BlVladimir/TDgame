class StateDamage:
    def __init__(self, type_bullet, func_array, damage_dict):
        self.__damage_dict = damage_dict
        self.__func_array = func_array
        self._type_bullet = type_bullet

    def __composition_push_functions(self, enemy, functions, dict_arguments):
        if len(functions) == 1:
            return functions[0](enemy, dict_arguments)
        return functions[0](enemy, self.__composition_push_functions(enemy, functions.pop(0), dict_arguments), dict_arguments)

    def push(self, enemy):
        self.__composition_push_functions(enemy, self.__func_array, self.__damage_dict)

    def improve_damage(self, type_damage, value):
        if type_damage in self.__damage_dict.keys():
            self.__damage_dict[type_damage]+=value

    def upgrade(self, visitor):
        visitor.visit_damage_state(self)