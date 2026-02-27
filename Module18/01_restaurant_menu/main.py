menu = 'утиное филе;фланк-стейк;банановый пирог;плов'

menu_list = [i if i != ';' else ', ' for i in menu]
print(('На данный момент в меню есть:', ''.join(menu_list).title()))


print(f'\n***************** Пример-2 **********************')

text = ''
for char in menu:
    if char != ';':
        text += char
    else:
        text += ', '
print(text.title())

print(f'**************** Принт-2 *******************')

print(', '.join(menu.title().split(';')))