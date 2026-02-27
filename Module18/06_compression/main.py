text = input('Введите текст: ')
new_text = ''
count = 1
for index in range(len(text)):
    if text.find(text[index], index + 1, len(text)) == index + 1 % len(text):
        count += 1
    else:
        new_text += ''.join([text[index], str(count)])
        count = 1
print(f'Закодированная строка {new_text}')
