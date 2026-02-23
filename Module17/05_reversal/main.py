text = input('Введите текст: ')
simbols = input('Введите символ, для поиска промежуточного результата: ')
if text.count(simbols) > 1:
    if len(text) > 2:
        print(text[text.rindex(simbols) - 1:text.index(simbols):-1])
    else:
        print(text[text.rindex(simbols):text.index(simbols):-1])
else:
    print(f'Символов {simbols} должно быть 2 и более в тексте {text}')


