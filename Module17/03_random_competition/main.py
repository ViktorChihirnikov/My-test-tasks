import random
list_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
list_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
list_3 = [list_1[i] if list_1[i] > list_2[i] else list_2[i] for i in range(len(list_1))]
print(f'Первая команда:{list_1}\nВторая команда:{list_2}\nПобедитель:{list_3}')
