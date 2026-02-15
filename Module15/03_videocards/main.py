list_video_cards = [3070, 2060, 3090, 3070, 3090]
new_list = []
max_num = 1

for card in list_video_cards:
    if card >= max_num:
        max_num = card

for i in list_video_cards:
    if i < max_num:
        new_list.append(i)
print(f'Старый список видеокарт {list_video_cards}\nНовый список видеокарт {new_list}')

print(f'\n****************** Пример-2 **********************')
print('Старый список:', list_video_cards)

max_value = max(list_video_cards)
count = 0
while count <= len(list_video_cards) - 1:
    if list_video_cards[count] == max_value:
        del list_video_cards[count]
    count += 1
print(f'Новый список {list_video_cards}')


