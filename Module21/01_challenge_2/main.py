def print_num(num):
    if num == 0:
        return
    print_num(num - 1)
    print(num)


number = int(input('Введите число: '))
print_num(number)
