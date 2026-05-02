from os import path
from collections.abc import Iterable
import random
import datetime


def make_error_log_file(arg_path: str) -> None:
    """
    Функция создаёт файл txt по указанной директории и записывает туда строки по условию если условие истина
    то в строке прописывается error и дата создания в остальных случаях COMPLETE: Данные успешно переданы
    :param arg_path: путь до файла
    :return: None
    """
    N = 20_000
    error_names = ['ValueError', 'ArithmeticError', 'AssertionError', 'ImportError', 'NameError', 'OSError']
    with open(arg_path, 'w+', encoding='utf8') as file:
        for _ in range(N):
            if random.randint(1, 10) == 5:
                text = 'ERROR: ' + random.choice(error_names) + ' ' + str(datetime.datetime.today())
            else:
                text = 'COMPLETE: Данные успешно переданы.'
            file.write(text + '\n')


def error_log_generator(path_file: str) -> Iterable[str]:
    """
    Функция генератор. Принимает путь и с помощью оператора with открывает файл для чтения.
    Генератор с условием, цикл for c аргументом открытый файл. По строчно считывается, строка проверяется и
     yield возвращаем нужную строку
    :param path_file: путь до файла
    :yield: Iterable[str]
    """
    with open(path_file, 'r', encoding='utf-8') as from_logs_file:
        for str_from_log_file in from_logs_file:
            if str_from_log_file.startswith('ERROR'):
                yield str_from_log_file




work_log_file_path = path.abspath(path.join('..', '..', 'Module26', '05_logs_processing', 'data', 'work_logs.txt'))
output_file_path = path.abspath(path.join('..', '..', 'Module26', '05_logs_processing', 'data', 'output_file'))


if not path.exists(work_log_file_path):
    make_error_log_file(work_log_file_path)
with open(output_file_path, 'w', encoding='utf-8') as output:
    for error_line in error_log_generator(work_log_file_path):
        output.write(error_line)
print("Файл успешно обработан.")




