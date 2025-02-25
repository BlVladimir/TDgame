class ConfigModifier:

    def __init__(self, is_free, price_up, type_new_modifier, influence):
        self.is_free = is_free
        self.price_up = price_up
        self.type_new_modifier = type_new_modifier
        self.influence = influence

    def get_price_up(self):
        return self.price_up

    def get_is_free(self):
        return self.is_free

    def get_type_new_modifier(self):
        return self.type_new_modifier

    def get_influence(self):
        return self.influence

    def get_new_value_price_up(self, new_value):
        self.price_up = new_value

    def get_new_value_is_free(self, new_value):
        self.is_free = new_value

    def get_new_value_type_new_modifier(self, new_value):
        self.type_new_modifier = new_value

    def get_new_value_influence(self, new_value):
        self.influence = new_value
