

def max_word(sentence):
    max_len_text = ''  # Для сохранения слова по длине
    text = ''  # Для создания слова
    for char in sentence:
        if char.isalpha():  # Условие для символа строки
            text += char  # Записываем символ исходя из условия

        else:
            if len(text) > len(max_len_text):  # Проверяем длину строки/слова
                max_len_text = text
                text = ''
    return max_len_text



text1 = input('Введите текст: ') + ' '  # Добавим пустую строку, что бы все слова попали под условие
result = max_word(text1)
print('Самое длинное слово: {}\nДлина слова {}'.format(result, len(result)))

print(f'\n********************* Пример-2 ***************************')
text2 = input('Введите текст: ').split()
print(f'Самое длинное слово: {max(text2, key=len)}\nДлина слова {len(max(text2, key=len))}')