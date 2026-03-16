def list_sort(lists):
    min_list = []
    same_list = []
    max_list = []
    value = lists[-1]

    for element in lists:
        if element < value:
            min_list.append(element)

        elif element == value:
            same_list.append(element)

        elif element > value:
            max_list.append(element)

    return min_list, same_list, max_list


def xorar(lists):
    if len(lists) < 2:
        return lists
    result_min, result_same, result_max = list_sort(lists)
    result_min = xorar(result_min)
    result_same = xorar(result_same)
    result_max = xorar(result_max)

    return result_min + result_same + result_max


b = [4, 9, 2, 7, 5]
test_list = [6, 5, 4, 3, 1, 0, 2]

result = xorar(test_list)
print(result)





