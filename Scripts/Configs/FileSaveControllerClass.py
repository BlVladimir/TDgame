class FileSaveController:
    def __init__(self):
        self.__file_save = 'Save'
        self.__base_file = ['alwaysUseAdditionalParameter = False\n',
                            'level = 0\n']

    def file_change(self, changed_parameter, new_value = True):  # изменяет значение в файле
        changed_parameter_line, parameters = self.__find_in_file(changed_parameter)
        if new_value:
            if parameters[changed_parameter_line].find('True') != -1:
                n = parameters[changed_parameter_line].find('True')
                parameters[changed_parameter_line] = parameters[changed_parameter_line][0:n-1] + 'False\n'
            elif parameters[changed_parameter_line].find('False') != -1:
                n = parameters[changed_parameter_line].find('True')
                parameters[changed_parameter_line] = parameters[changed_parameter_line][0:n-1] + 'True\n'
            else:
                new_value = 'reset settings'
        else:
            n = parameters[changed_parameter_line].find('=')
            parameters[changed_parameter_line] = parameters[changed_parameter_line][0:n + 1] + str(new_value) + '\n'
        file_save = open(self.__file_save, 'w')
        if new_value == 'reset settings':
            for i in self.__base_file:
                file_save.write(i)
        else:
            for i in parameters:
                file_save.write(i)
        file_save.close()

    def reset_settings(self):
        file_save = open(self.__file_save, 'w')
        for i in self.__base_file:
            file_save.write(i)
        file_save.close()

    def __find_in_file(self, parameter):  # находит значение в файле
        file_save = open(self.__file_save, 'r')
        parameters = file_save.readlines()
        file_save.close()
        for i in range(len(parameters)):
            if parameters[i].find(parameter) != -1:
                return i, parameters
        self.reset_settings()

    def get_level(self):
        additional_parameter_parameter_line, parameters = self.__find_in_file('level = ')
        if parameters[additional_parameter_parameter_line].find('1') != -1:
            return 1
        elif parameters[additional_parameter_parameter_line].find('2') != -1:
            return 2
        elif parameters[additional_parameter_parameter_line].find('2') != -1:
            return 3
        elif parameters[additional_parameter_parameter_line].find('2') != -1:
            return 4
        elif parameters[additional_parameter_parameter_line].find('2') != -1:
            return 5
        elif parameters[additional_parameter_parameter_line].find('2') != -1:
            return 6

    def get_always_use_additional_parameter(self, context):
        context.get_config_gameplay().set_always_use_additional_parameters(self.find_always_use_additional_parameter())

    def find_always_use_additional_parameter(self):
        additional_parameter_parameter_line, parameters = self.__find_in_file('alwaysUseAdditionalParameter = ')
        if parameters[additional_parameter_parameter_line].find('True') != -1:
            return False
        else:
            return True
