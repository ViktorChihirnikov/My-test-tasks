def search(passed_text):
    char_count = {}
    for char in passed_text:
        char_count[char] = char_count.get(char, 0) + 1
    count = 0
    for value in char_count.values():
        if value % 2 != 0:
            count += 1
    return count <= 1


text = input('Введите текст: ')
if search(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

