nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def one_list(lists):
    new_list = []
    for element in lists:
        if isinstance(element, int):
            new_list.append(element)
        if isinstance(element, list):
            new_list.extend(one_list(element))
    return new_list

result = one_list(nice_list)

print(f'Ответ: {result}')


def merge_list(passed_list, index=0):
    new_list = []
    # Значение списка
    value = passed_list[index % len(passed_list)]
    # Условие для выхода
    if index == len(passed_list):
        return new_list
    # Проверка значения по типу данных и добавление в новый список
    elif isinstance(value, int):
        new_list.append(value)
    # Проверка значения по типу данных, вызова рекурсии, расширения списка
    elif isinstance(value, list):
        new_list.extend(merge_list(value))
    # Вызов рекурсии для прохода по индексу в списке
    new_list.extend(merge_list(passed_list, index + 1))
    return new_list


print(f'Ответ: {merge_list(nice_list)}')

