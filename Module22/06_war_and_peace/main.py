import zipfile
import os
import string


def unpacking_zip(path, pattern=None):
    with zipfile.ZipFile(path) as myzip:
        for name_file in myzip.infolist():
            if pattern and name_file.filename.endswith(pattern):
                path_txt = myzip.extract(name_file)
            else:
                path_txt = myzip.extract(name_file)
        return path_txt


def sort_file_txt(path):
    type_dict = {'english_simbols': {}, 'rus_simbols': {}}
    with open(path, 'r', encoding='utf-8') as read_file:
        # Цикл по строкам
        for line in read_file:
            # Цикл по символам строки
            for char in line.strip():
                if char.isalpha():
                    if char in string.ascii_letters:
                        type_dict['english_simbols'][char] = type_dict['english_simbols'].get(char, 0) + 1
                    else:
                        type_dict['rus_simbols'][char] = type_dict['rus_simbols'].get(char, 0) + 1

        return type_dict


def print_result(data):
    for name_language in result_sort.keys():
        sort_dict = sorted(result_sort[name_language].items(), key=lambda x: -x[1])
        print(name_language.upper())
        for key, value in sort_dict:
            print(key, value)
        print()


path_file = os.path.abspath(os.path.join('voina-i-mir.zip'))
if zipfile.is_zipfile(path_file):
    unpacking_file = unpacking_zip(path_file)
    result_sort = sort_file_txt(unpacking_file)
    print_result(result_sort)

elif os.path.isfile(path_file):
    result_sort = sort_file_txt(path_file)
    print_result(result_sort)


