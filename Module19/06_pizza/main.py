info_dict = {}
count = int(input('Введите количество раз для ввода информации: '))
for _ in range(1, count + 1):
    print('Введите информацию: Имя, название товара, кол-во, через пробел: ', end='')
    name, pizza, count_pizza = input().title().split()

    if name not in info_dict:
        info_dict[name] = {pizza: int(count_pizza)}
    else:
        if pizza in info_dict[name]:
            info_dict[name][pizza] += int(count_pizza)
        else:
            info_dict[name].update({pizza: int(count_pizza)})

for i_key in sorted(info_dict):
    print(i_key)
    for i_k, i_v in sorted(info_dict[i_key].items()):
        print('    ', i_k, ':', i_v)

