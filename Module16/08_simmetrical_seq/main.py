def examination_list(arr):
    count = 0
    result = []
    if arr == arr[::-1]:
        print('Менять ни чего не нужно!!!')
        return count, result

    else:
        index_insert = len(arr)  # Индекс для вставки
        print('Последовательность:', arr)
        while arr != arr[::-1]:  # Условие проверки
            arr.insert(index_insert, arr[count])  # Вставка значения по индексу
            result.insert(0, arr[count])  # Вставка по индексу добавленных значений
            count += 1
        return count, result


list_num = [1, 2, 3]
count_num, result_list = examination_list(list_num)
print('Кол-во чисел, нужно добавить {}\nИ сами числа: {}'.format(count_num, result_list))

print(f'\n******************** Пример-2 *****************************')

list_num1 = [1, 2, 3]
if list_num1 == list_num1[::-1]:
    print('Менять ни чего не надо!!!!')
else:
    print('Последовательность', list_num1)
    count_num = 0
    insert_num = len(list_num1)
    add_numbers = []
    while list_num1 != list_num1[::-1]:
        list_num1.insert(insert_num, list_num1[count_num])
        add_numbers.insert(0, list_num1[count_num])
        count_num += 1
    print('Кол-во чисел, нужно добавить {}\nИ сами числа {}'.format(count_num, add_numbers))




