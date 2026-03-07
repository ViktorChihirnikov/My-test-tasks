def result(dict_simbols):
    count = max(dict_simbols.values())
    invent_dict = {}
    for i_count in range(1, count + 1):
        invent_dict[i_count] = [key for key in dict_simbols if dict_simbols[i_key] == i_count]
    return invent_dict


text = 'Здесь что-то написано'#input('Введите текст: ')
new_dict = {}
for char in text:
    new_dict[char] = new_dict.get(char, 0) + 1
invent_for_for = result(new_dict)

for i_key, i_value in invent_for_for.items():
    print(i_key, ':', i_value)
