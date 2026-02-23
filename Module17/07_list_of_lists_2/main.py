nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

print(f'Ответ: {[value for list_values in nice_list for list1 in list_values for value in list1]}')

# Пример работы ls
new_list = []
for i in nice_list:
    for j in i:
        for value in j:
            new_list.append(value)
print(new_list)
