list_name =['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
list1 =[]
list2 = []

for index, name in enumerate(list_name):
    if index % 2 == 0:
        list1.append(name)
    else:
        list2.append(name)
print(f'Первый день: {list1}\nВторой день: {list2}')

print(f'\n*************** Пример-2 **********************')
list1 = [list_name[index] for index in range(0, len(list_name), 2)]
list2 = [list_name[index] for index in range(1, len(list_name), 2)]
print(f'Первый день: {list1}\nВторой день: {list2}')


