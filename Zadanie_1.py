# Мусулезный Максим 15.07.2023
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Вариант 1

def split_path(abs_path: str) -> tuple():
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[1]
    return path, name, expansion

# Вариант 2

import os

def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)