violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

choice_count_list = int(input('Укажите количество песен: '))
teams = 0
for num in range(1, choice_count_list + 1):
    choice = input(f'Название {num}-й песни: ')
    for value in violator_songs:
        if choice in value:
            teams += value[1]

print(f'Общее время звучания: {teams:.2f}')


