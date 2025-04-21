import sys
import os

def resource_path(relative_path):
    """ Преобразует пути к ресурсам для работы в EXE и из исходников """
    try:
        base_path = sys._MEIPASS  # Папка временных файлов PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    full_path = os.path.join(base_path, relative_path)
    if not os.path.exists(full_path):
        print(f"Файл не найден: {full_path}")
        print(f"Текущая рабочая директория: {os.getcwd()}")
        print(f"Содержимое папки: {os.listdir(os.path.dirname(full_path))}")

    return full_path