
count_letters = 0
list_error = []

with (open('people.txt', 'r+', encoding="utf-8") as file_people,
      open('errors.log', 'w', encoding='utf-8') as file_errors):

    for index, i_element in enumerate(file_people, 1):
        try:
            count_letters += len(i_element.strip())
            if len(i_element.strip()) < 3:
                list_error.append(index)
                raise ValueError('B файле people.txt в слове {} менее 3 значений'.format(i_element))
        except ValueError as exc:
            file_errors.write(str(exc) + '\n')

    print(f'Менее 3 символов в строке: {"-".join(map(str, list_error))}')
    print(f'Общее количество букв: {count_letters}')
