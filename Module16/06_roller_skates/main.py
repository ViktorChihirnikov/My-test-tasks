size_lict = [41, 40, 39, 42]
people_size = [42, 41, 42]

max_count = 0
for i in size_lict:
    if i in people_size:
        max_count += 1
print('\nНаибольшее ко-во людей, которые могут взять коньки', max_count)



print(f'\n*************** Пример-2 ********************************')
print('С использованием set')
people_can_have_roller_skates = len(set(size_lict) & set(people_size))
print('Наибольшее ко-во людей, которые могут взять коньки: {}'.format(people_can_have_roller_skates))