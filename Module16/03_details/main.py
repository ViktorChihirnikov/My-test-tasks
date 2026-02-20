shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Введите названия: ').lower()
count = 0
summ = 0
was_price = 0
for value, price in shop:
    if name == value:
        count += 1
        print('{} Название товара: {} цена: {}'.format(count, value, price))
        summ += price

print(f'В наличии  {name} - {count}\nОбщая стоимость - {summ}')

