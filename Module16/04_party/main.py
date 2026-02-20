guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
entrance = 'пришёл'
exits = 'ушёл'
stop = 'пора спать'

while True:
    sum_guest = len(guests)
    print(f'\nСейчас на вечеринке {sum_guest} человек {guests}')
    choice = input(f'Пришёл человек или ушёл? ')
    name = input(f'Как ваше Имя? ').title()
    if choice == entrance:
        if sum_guest < 6:
            guests.append(name)
            print(f'Добро пожаловать на нашу тусу, {name})')
        else:
            print(f'\nИзвините, у нас полна горница людей! Пошёл вон)')

    elif choice == exits:
        if name in guests:
            guests.remove(name)
            print(f'Приятно было вас видеть, до свидания.')
        else:
            print(f'Такого имени {name} нет в списке, наверно много выпили.')

    elif choice == stop:
        print(f'Команда была спать, все легли спать')
        break
