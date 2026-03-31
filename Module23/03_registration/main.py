def error_string(count, string):
    try:
        if len(string.split()) < 3:
            raise IndexError(f'В строке не присутствует вся информация! Номер строки - {count}')
        name, email, age = string.strip().split()
        if not name.isalpha():
            raise NameError(f'Поле  "Имя" содержит не только буквы. Строка - {count}')
        elif '@' not in email or '.' not in email:
            raise SyntaxError(f'Поле "Емэйл"  не содержит @ или .(точка). Строка - {count}')
        elif int(age) > 99 or int(age) < 10:
            raise ValueError(f'Поле "Возраст" не является числом от 10 до 99 Строка - {count}')
    except (IndexError, NameError, SyntaxError, ValueError) as exc:
        return exc


with (open('registrations.txt', 'r', encoding='utf-8') as registration_file,
     open('registrations_bad.log', 'w', encoding='utf-8') as bad_file,
     open('registrations_good.log', 'w', encoding='utf-8') as good_file):

    for index, i_string in enumerate(registration_file, 1):
        result_function = error_string(index, i_string)
        if result_function:
            bad_file.write(f'{i_string.strip()} - {str(result_function)}\n')
        else:
            good_file.write(str(i_string))

    print('Проверка закончена, проверьте файлы!!!')



