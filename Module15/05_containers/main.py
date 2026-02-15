list_container = []
count = 0
container_sum = int(input('Введите количество контейнеров: '))
while count != container_sum:
    new_container = int(input('Введите вес контейнера: '))
    if new_container > 200:
        print('Вес не должен превышать 200 кг')
    else:
        for value in list_container:
            if new_container <= value:
                list_container.insert(count + 1, new_container)
                print(f'Номер нового контейнера будет {count + 1}')
                count += 1
                break
        else:
            list_container.insert(0, new_container)
            print(f'Номер нового контейнера будет 1')
            count += 1
print(list_container)




