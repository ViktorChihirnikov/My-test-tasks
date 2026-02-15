

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [-20, 14, 3, 18, 21, -12, 9, 6]
index = 0
while index != len(numbers_list):
    if numbers_list[index] % 2 == 0:
        numbers_list.insert(0, numbers_list.pop(index))
        index += 1
    else:
        del numbers_list[index]
        index = index % len(numbers_list)


print(f'Изменённый список {numbers_list}')

print(f'\n***************** Пример-2 **************************')
numbers = [-20, 14, 3, 18, 21, -12, 9, 6]
index = len(numbers) - 1
while index != -1:
    if numbers[index] % 2 == 0:
        print((numbers[index]), end=' ')
    index -= 1
print()