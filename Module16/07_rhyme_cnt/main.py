count_people = int(input('Кол-во человек: '))
del_num = int(input('Число считалки на выбывания: '))
num_people_list = list(range(1, count_people + 1))
print(f'Значит, выбывает каждый {del_num} человек')

index = 0
while len(num_people_list) > 1:
    print('\nТекущее число людей', num_people_list)
    print('Счёт начинается с номера ', num_people_list[index])
    index = (index + del_num - 1) % len(num_people_list)
    print('Выбывает человек под номером', num_people_list.pop(index))
    index = index % len(num_people_list)

print('\nОстаётся человек под номером', num_people_list[0])













