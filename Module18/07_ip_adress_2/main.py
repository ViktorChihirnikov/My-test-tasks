ip_address = '256.12.12,5'#input('Введите ip address: ').split('.')
address = ip_address.split('.')

choice = True
for num in address:
    if not num.isdigit() and ',' not in num:
        print(num, '-Это не целое число!!')
        choice = False

    elif num.isnumeric() and int(num) > 255:
        print(num, '- число не может быть больше 255')
        choice = False

    elif ',' in num:
        print(num, 'Адрес, это числа через точку. Пример - 128.22.33.04  ')
        choice = False

if choice:
    if len(address) > 4 or len(address) < 4:
        print(address, 'Слишком длинный или короткий адрес!!!!')
    else:
        print('Адрес указан верный')
