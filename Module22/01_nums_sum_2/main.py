import os


def sum_elements_of_file(data, name_file):
    summ = 0
    print('Содержимое файла: {}'.format(name_file))
    for line in data:
        print(line)
        for element_list in line.strip().split():
            if element_list.isdecimal():
                summ += int(element_list)
    return str(summ)


path_number_txt = os.path.abspath(os.path.join('numbers.txt'))
path_answer_txt = os.path.abspath(os.path.join('answer.txt'))

data_numbers_txt = open(path_number_txt, 'r', encoding='utf-8')
result = sum_elements_of_file(data_numbers_txt, os.path.basename(path_number_txt))
data_numbers_txt.close()

answer_txt = open(path_answer_txt, 'w', encoding='utf-8')
answer_txt.write(result)
print(f'Содержимое файла: {os.path.basename(path_answer_txt)}\n{result}')
answer_txt.close()



















