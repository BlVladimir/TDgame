import json
import os
import sys
from pathlib import Path


class FileSaveController:
    def __init__(self):
        self.__file_save = self.__get_save_path()
        self.__base_data = {
            'always use additional parameter': False,
            'level': 1,
            'play_sound': True,
            'play_music': True
        }
        self.__ensure_save_file_exists()

    def __get_save_path(self):
        """Определяет правильный путь к файлу сохранения для EXE и разработки"""
        if getattr(sys, 'frozen', False):
            # Для EXE файла - сохраняем рядом с исполняемым файлом
            base_dir = Path(sys.executable).parent
        else:
            # Для разработки - в папке проекта
            base_dir = Path(__file__).parent

        save_dir = base_dir / "save"
        save_dir.mkdir(exist_ok=True)  # Создаем папку, если не существует
        return save_dir / "save.json"

    def __ensure_save_file_exists(self):
        """Создает файл сохранения с базовыми значениями, если его нет"""
        if not os.path.exists(self.__file_save):
            with open(self.__file_save, 'w', encoding='utf-8') as file:
                json.dump(self.__base_data, file, indent=4)

    def get_parameter(self, parameter_name):
        """Безопасное получение параметра"""
        try:
            with open(self.__file_save, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get(parameter_name, self.__base_data.get(parameter_name))
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            return self.__base_data.get(parameter_name)

    def set_parameter(self, parameter_name, new_value):
        """Безопасная установка параметра"""
        try:
            with open(self.__file_save, 'r', encoding='utf-8') as file:
                data = json.load(file)

            data[parameter_name] = new_value

            with open(self.__file_save, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Ошибка записи в файл: {e}")

    def change_true_false(self, parameter_name):
        """Переключение boolean-параметра"""
        current_value = self.get_parameter(parameter_name)
        self.set_parameter(parameter_name, not current_value)