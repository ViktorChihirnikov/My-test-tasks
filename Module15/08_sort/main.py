list1 =[3, 2, -3, 0, 5]

print('Изначальный  список:', list1)
# buble_sort
for i in range(len(list1)):
    # Флаг для того, если список отсортирован то после первой итерации остановится
    flag = False
    # Проходим по списку и если 1-е значение больше второго то меняем их местами
    for index2 in range(0, len(list1) - 1):
        if list1[index2] > list1[index2 + 1]:
            list1[index2], list1[index2 + 1] = list1[index2 + 1], list1[index2]
            flag = True
    if not flag:
        break

print('Отсортированный список:', list1)


print(f'\n********************* Пример-2 *************************')
# selection_sort
list2 = [3, 0, -1, -3, 4, 1, -10, 39, 36]
print('Изначальный  список:', list2)
# Цикл для прохода по списку и генерации значения для вложенного цикла в start.
for index1 in range(len(list2) - 1):
    # Индекс минимального значения
    min_index = index1
    # Вложенный цикл для генерации индексов
    for index2 in range(index1 + 1, len(list2)):
        # Условие, если значение больше следующего то берём индекс от минимального значения и
        # проверяем уже его
        if list2[min_index] > list2[index2]:
            min_index = index2
    # После прохода по списку, находим индекс минимального значение и перезаписываем его
    list2[index1], list2[min_index] = list2[min_index], list2[index1]

print('Отсортированный список', list2)

print(f'\n********************* Пример-3 *********************')
# Insert_sort
list3 = [10, 2, 0, -2, 5, 30, 3]
print(f'Начальный список: {list3}')
# Берём длину списка
run = len(list3)
# Циклом проходим по длине списка от 1, и берём значения для проверки в key
for i in range(1, run):
    key = list3[i]
    # Задаём индекс для прохода по списку от 0
    index = i - 1
    # Цик с проверкой пока индекс >= 0 и ключ/это последующие значение по отношению к проверяемому < значения из списка
    while index >= 0 and key < list3[index]:
        list3[index + 1] = list3[index]
        index -= 1
    list3[index + 1] = key

print(list3)


