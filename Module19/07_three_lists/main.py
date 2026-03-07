array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


print('ЗАДАНИЕ 1')
print(f"Решение без множеств: {', '.join(sorted([str(num) for num in array_3 if num in array_1 and num in array_2]))}")
print(f"Решение со множествами: {', '.join(sorted([str(i) for i in set(array_1) & set(array_3) & set(array_2)]))}\n")
print('ЗАДАНИЕ 2')
print(f"Решение без множеств: {', '.join(sorted([str(i) for i in array_1 if i not in array_2 and i not in array_3]))}")
print(f"Решение со множествами: {', '.join(sorted([str(i) for i in(set(array_1) - set(array_2) - set(array_3))]))}")



array_4 = [1, 5, 10, 20, 40, 80, 100]
array_5 = [6, 7, 20, 80, 100]
array_6 = [3, 4, 15, 20, 30, 70, 80, 120]
print(','.join([str(num) for num in array_6 if num in array_5 and array_4]))
print(sorted(set(array_6) & set(array_5) & set(array_4)))
print(sorted(set(array_4) - set(array_5) - set(array_6)))