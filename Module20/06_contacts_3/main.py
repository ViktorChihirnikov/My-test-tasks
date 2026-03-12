telephone_book = {}
while True:
    print(f'Выберите действие\n   1.Добавить контакт\n   2.Найти по фамилии')
    choice = int(input('Ввод: '))
    if choice == 1:
        name = tuple(input('Введите Имя и Фамилию через пробел: ').title().split())
        if name in telephone_book:
            print('Такой контакт уже есть!')
        else:
            telephone_book[name] = int(input('Введите номер: '))
            print(f'{telephone_book}')

    elif choice == 2:
        surname = input('Введите фамилию: ').title()
        if telephone_book:
            for key, value in telephone_book.items():
                if surname in key[1]:
                    print(f'{" ".join(key)} - {value}')
        else:
            print('Список пуст!')
