# TODO здесь писать код
def sort_tuple(passed_tuple):
    for value in passed_tuple:
        if isinstance(value, float):
            return passed_tuple

    return sorted(passed_tuple, reverse=False)


tpl = (6, 3, -1, 8, 4, 10, -5)
print(sort_tuple(tpl))
#Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)





