def sum_number(a):
    summ = 0
    while a > 0:
        summ += a % 10
        a //= 10
    return summ


def count_number(a):
    count = 0
    while a > 0:
        a //= 10
        count += 1
    return count


number = int(input('Введите число: '))
print(f'\nСумма чисел {sum_number(number)}')
print(f'Количество цифр в числе {count_number(number)}')
print(f'Разность суммы и количества цифр {abs(sum_number(number) - count_number(number))}')
