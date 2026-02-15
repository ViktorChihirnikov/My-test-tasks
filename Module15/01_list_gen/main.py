number = int(input('Введите число: '))
list_numbers =[]

for num in range(1, number + 1):
    if num % 2 != 0:
        list_numbers.append(num)
print('Список из нечётных чисел от 1 до', number, list_numbers)

print(f'\n********************** Пример-2 *********************')
list_numbers =[]
for num in range(1, number + 1, 2):
    list_numbers.append(num)
print('Список из нечётных чисел от 1 до', number, list_numbers)

print(f'\n************* Пример-3 ************************')
print(f'Список из нечётных чисел от 1 до {number} {list(range(1, number, 2))}')