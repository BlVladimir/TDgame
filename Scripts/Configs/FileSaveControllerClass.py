import json

class FileSaveController:

    def __init__(self):
        self.__file_save = 'save.json'
        self.__base_data = {'always use additional parameter': False, 'level': 1}

    def get_parameter(self, parameter_name):
        with open(self.__file_save, 'r', encoding='utf-8') as file:
            data = json.load(file)
        parameter_value = data[parameter_name]
        return parameter_value

    def set_parameter(self, parameter_name, new_value):
        with open(self.__file_save, 'r', encoding='utf-8') as file:
            data = json.load(file)
        data[parameter_name] = new_value
        with open(self.__file_save, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def change_true_false(self, parameter_name):
        with open(self.__file_save, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if data[parameter_name]:
            self.set_parameter(parameter_name, False)
        else:
            self.set_parameter(parameter_name, True)