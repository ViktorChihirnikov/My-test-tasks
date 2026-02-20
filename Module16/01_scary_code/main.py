def delite(num_list, num):
    for _ in range(num_list.count(num)):
        num_list.remove(num)
    return num_list


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
print(f'Первое объединение. Количество чисел 5: {a.count(5)}')
delite(a,5)
a.extend(c)
print(f'\nВторое объединение. Количество чисел 3: {a.count(3)}\nОбновлённый список:{a}')








