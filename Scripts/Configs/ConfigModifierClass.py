class ConfigModifier:

    def __init__(self, is_free, price_up, type_new_modifier, influence):
        self.__is_free = is_free
        self.__price_up = price_up
        self.__type_new_modifier = type_new_modifier
        self.__influence = influence

    def get_price_up(self):
        return self.__price_up

    def get_is_free(self):
        return self.__is_free

    def get_type_new_modifier(self):
        return self.__type_new_modifier

    def get_influence(self):
        return self.__influence

    def get_new_value_price_up(self, new_value):
        self.__price_up = new_value

    def get_new_value_is_free(self, new_value):
        self.__is_free = new_value

    def get_new_value_type_new_modifier(self, new_value):
        self.__type_new_modifier = new_value

    def get_new_value_influence(self, new_value):
        self.__influence = new_value
