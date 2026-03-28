import string


def sort_char(file):
    with open(file, 'r', encoding='utf-8') as read_file:
        result_dict = {}
        for line in read_file:
            for char in line.strip():
                if char.lower() in string.ascii_lowercase:
                    result_dict[char.lower()] = result_dict.get(char.lower(), 0) + 1

        return result_dict


def write_sort_dict_and_print_result(data, path):
    with open(path, 'w', encoding='utf-8') as write_file:
        count_char = sum(data.values())
        for i_char, i_value in sorted(data.items(), key=lambda items: (-items[1], items[0])):
            write_file.write(f'{i_char} - {round(i_value / count_char, 3)}\n')
            print(f'{i_char} - {round(i_value / count_char, 3)}')



result_sort = sort_char('text.txt')
write_sort_dict_and_print_result(result_sort, 'analysis.txt')
