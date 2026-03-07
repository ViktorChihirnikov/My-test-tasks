violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
sum_team = 0
count = int(input('Сколько песен нужно посмотреть: '))
for _ in range(count):
    name = input('Введите название песни: ')
    if name not in violator_songs.keys():
        print('Нет такой песни!')
    sum_team += violator_songs.get(name, 0)
print(f'Общее время звучание треков: {round(sum_team, 3)} мин')


print(f'\n********************* Пример-2 **********************')
teams = 0
count = int(input('Сколько песен нужно посмотреть: '))
for _ in range(count):
    name = input('Введите название песни: ').upper()
    for sing in violator_songs.keys():
        if sing.upper() is name:
            teams += violator_songs[sing]
            break

    else:
        print('Нет такой песни!!!!!')

print(f'Общее время звучание треков: {sum_team:.2f} мин')

