number = int(input('Введите число для генерации списка: '))

print([1 if num % 2 == 0 else num % 5 for num in range(number)])
