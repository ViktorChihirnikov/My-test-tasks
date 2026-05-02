import os
from collections.abc import Iterable


def search_and_count(path_direct: str) -> Iterable[int]:
    """
    Функция генератор возвращает объект генератора с использованием рекурсивной функции walk()
    функция walk() возвращает кортеж: (Путь до каталога, Список подкаталогов, Список файлов в каталоге)
    :param path_direct: str
    :return: Iterable[int]
    """
    for path_direct, list_direct, list_files in os.walk(path_direct):
        # Генераторное выражение с условием.
        for file in (element for element in list_files if element.endswith('py')):
            # Путь до файла
            path_file = os.path.join(path_direct, file)
            # Оператор with, открывает файл для чтения
            with open(path_file, 'r', encoding='utf-8') as file_count:
                count_line = 0
                # С помощью цикла фор проходим по строчно
                for line in file_count:
                    # С помощью метода strip обрезаем начало строки
                    line = line.strip(' ')
                    # Условие, с применением метода startswith и передаём кортеж с символами
                    # для исключения не нужных строк из файла
                    if not line.startswith(('#', '\n')):
                        count_line += 1
                yield f'В директории {os.path.basename(path_direct)}\n  В файле {os.path.basename(path_file)} {count_line} - строк\n'


# path_input = input('Введите директорию для поиска файла ')
for count_str in search_and_count(os.path.abspath(os.path.join('..', '..', 'Module26'))):
    print(count_str)
