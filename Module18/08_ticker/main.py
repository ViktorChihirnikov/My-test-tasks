text = 'abcd'
text_1 = 'cdab'
a = ''
count = 0
while text != text_1:
    a = ''.join([text_1[len(text_1) - 1], text_1[0:len(text_1) - 1]])
    text_1 = a
    count += 1
    if count > 3:
        print('Нельзя выровнять порядок значений через сдвиг')
        break
else:
    print('Количество сдвигов будет:', count)

