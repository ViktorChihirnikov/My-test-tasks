while True:
    ciph = input('Придумайте пароль из 8 символов. Из них, одна большая буква и три цифры: ')

    upper_simbols = [i.isupper() for i in ciph].count(True)
    simbols_int = [i.isdecimal() for i in ciph].count(True)
    print(upper_simbols, simbols_int)

    if upper_simbols > 0 and simbols_int >= 3 and len(ciph) >= 8:
        print('Пароль надёжный')
    else:
        print('Ненадёжный пароль!')


