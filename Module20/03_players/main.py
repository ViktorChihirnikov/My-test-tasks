players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


new_list = [i_key + i_values for i_key, i_values in players.items()]
print('Новый список из кортежа', new_list)


