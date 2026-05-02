import os
from collections.abc import Iterable


def gen_files_path(get_path: str, name_map: str) -> Iterable[str]:
    """
    Функция генератор возвращает объект генератора с использованием рекурсивной функции walk()
     функция walk() возвращает кортеж: (Путь до каталога, Список подкаталогов, Список файлов в каталоге)
    :param get_path: str:
    :param name_map: str
    :return: Iterable[str]
    """
    for path, lists, name in os.walk(get_path):
        # Условие для нахождения каталога и возвращает путь
        if os.path.basename(path) == name_map:
            yield f'Путь искомого каталога {path}'
        else:
            print(f'\nПути до файлов в каталоге {os.path.basename(path)}')
            # Условие для проверки, если в каталоге есть файлы то возвращаем путь, если нет то выводим сообщение.
            if name:
                # Генератор путей до фала из сгенерированного списка
                for file in name:
                    yield os.path.join(path, file)
            else:
                yield f'Каталог {os.path.basename(path)} пустой!!!\n'





# Путь к главному диску
path_1 = os.path.abspath(os.path.join(os.path.sep))

for result in gen_files_path(path_1, 'Python_Basic'):
    print(result)
