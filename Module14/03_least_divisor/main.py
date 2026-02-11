def min_divider(num):
    result = 0
    for divider in range(2, num + 1):
        if num % divider == 0:
            result = divider
            break
    return result


number = int(input('Введите число: '))
print(f'Наименьший делитель отличный от единицы {min_divider(number)}')
