text = input('Введите текст: ')  # 'Нужно отнести кольцо в Мордор'

vowels_simbols = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']

text_simbols = [i for i in text if i in vowels_simbols]

print(f'Список гласных букв {text_simbols}\nКол-во {len(text_simbols)}')

