
import random
origin = list(range(10))
new_list_0 = list(zip(origin[0: len(origin): 2], origin[1: len(origin): 2]))
new_list_01 = [(i, v) for i, v in zip(origin[0: len(origin): 2], origin[1: len(origin): 2])]

new_list_2 = [(origin[i % len(origin)], origin[i + 1 % len(origin)]) for i in range(0, len(origin), 2)]

new_list_3 = [(value, origin[index + 1]) for index, value in enumerate(origin) if index % 2 == 0]
print('Оригинальный список', origin)
print('1-й вариант:', new_list_01)
print('2-й вариант:', new_list_2)
print('3-й вариант:', new_list_3)
