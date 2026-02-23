def cipher(text, step):
    rus_simbols = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    cipher_text = ''
    for value in text:
        if not value.isalpha():
            cipher_text += value
        else:
            index = rus_simbols.index(value) + step
            cipher_text += rus_simbols[index % len(rus_simbols)]
    return cipher_text


text_for_cipher = input('Введите текст для шиф-ния: ')
shift = int(input('Введите сдвига: '))
result = cipher(text_for_cipher, shift)
print(f'Зашифрованный текст {result}')

