goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for name, value in goods.items():
    summ = 0
    summ_name = 0
    for i_count in range(len(store[value])):
        summ_name += store[value][i_count]['quantity']
        summ += store[value][i_count]['quantity'] * store[value][i_count]['price']
    print(f'{name} - {summ_name} штук. Стоимость {summ}')
