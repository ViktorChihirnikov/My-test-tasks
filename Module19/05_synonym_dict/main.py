
new_dict = {}
count = int(input('Сколько пар слов хотите добавить, указать число: '))
while count > 0:
    print(f'Введите пару слов через пробел:  ', end='')
    text = input().title().split()
    # Множество ключей и значений
    all_values_from_dict = set(new_dict).union(set(new_dict.values()))
    # Проверка на нахождение слова в словаре
    if text[0] in all_values_from_dict or text[1] in all_values_from_dict:
        print('Уже были добавлены!')
    else:
        new_dict[text[0]] = text[1]
        count -= 1

search = input('Введите слово: ').title()
print('Синоним:', new_dict.get(search, 'Такого слова нет'))



