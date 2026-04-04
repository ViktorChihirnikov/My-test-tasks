import random

stop = 776
start = 0


with open('out_file.txt', 'w', encoding='utf-8') as out_file:
    while start < stop:
        try:
            next_number = int(input('Введите число: '))
            result_random = random.randint(1, 13)
            if result_random == 1:
                raise Warning('На этот раз вам не повезло!')
            out_file.write(str(next_number) + '\n')
            start += next_number
        except Warning as exc:
            print(exc)
            break
    else:
        print('Удача на вашей стороне!')






