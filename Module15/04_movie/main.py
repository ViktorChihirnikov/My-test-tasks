films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_list =[]
quantity_films = len(films)
choice = int(input('\nСколько фильмов хотите выбрать? '))
if choice > quantity_films:
    print(f'В списке только {quantity_films} фильмов!')
else:
    count = 0
    while count != choice:
        film = input('Какой фильм хотите посмотреть: ').title()
        if film in films:
            if film in favorite_list:
                print(f'Фильм {film} уже добавлен в ваш список!!!!')
            else:
                favorite_list.append(film)
                count += 1
        else:
            print(f'Такого фильма {film} нет в списке')
    print('Ваш список любимых фильмов: ', ', '.join(favorite_list))
