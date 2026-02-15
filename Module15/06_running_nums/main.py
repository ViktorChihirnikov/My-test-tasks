
list_numbers = [1, 2, 3, 4, 5]
step = int(input('Введите сдвиг: '))
# Цикл, который создаёт количество сдвигов
for _ in range(1, step + 1):
    # Сохраняем значение которое нужно буде сдвинуть
    key = list_numbers[-1]
    # Переменные в которых будут предыдущее значение и последующие
    last_num = list_numbers[0]
    second_num = 0

    for index in range(0, len(list_numbers) - 1):
        # Сохраняем значение, которое перезапишется на предыдущие
        second_num = list_numbers[index + 1]
        # Перезаписываем значение на предыдущее
        list_numbers[index + 1] = last_num
        # Сохраняем перезаписанное значение
        last_num = second_num
    # После прохода по циклу вставляем в начала цикла ключ/ число которое должно сдвигаться на каждой итерации
    list_numbers[0] = key
print(list_numbers)

print(f'\n******************** Пример-2 *******************************')
new_list = [1, 2, 3, 4, 5]
for _ in range(step):
    index = 0
    last_value = new_list[0]
    second_value = 0
    while index != len(new_list):
        second_value = new_list[(index + 1) % len(new_list)]
        new_list[(index + 1) % len(new_list)] = last_value
        last_value = second_value
        index += 1
print(new_list)


print(f'\n***************** Пример-3 **********************')

list1 = list(range(1, 6))
count = 0
while count != step:
    list1.insert(0, list1.pop(-1))
    count += 1
print(list1)
