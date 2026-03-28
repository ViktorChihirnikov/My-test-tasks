import os


def search_file_direct(path_direct):
    under_direct = 0
    count_file = 0
    sum_size_file = 0
    for i_element in os.listdir(path_direct):
        path = os.path.join(path_direct, i_element)
        if os.path.isfile(path):
            count_file += 1
            sum_size_file += os.path.getsize(path)
        elif os.path.isdir(path):
            under_direct += 1
            under, count, summ = search_file_direct(path)
            under_direct += under
            count_file += count
            sum_size_file += summ
    return under_direct, count_file, sum_size_file


path_module = os.path.abspath(os.path.join('..', '..', 'Module22'))

under_dir, count_files, size = search_file_direct(path_module)

print(f'Размер каталога:{round((size / 1024), 1)} килобайт.\nКоличество файлов:{count_files}\nКоличество подкаталогов:{under_dir}')




