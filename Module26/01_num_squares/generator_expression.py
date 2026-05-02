# Генераторное выражение не создаёт последовательность целиком, а создаёт по одному числу
# из последовательности

generator = (num ** 2 for num in range(1, 11))

for num in generator:
    print(num)