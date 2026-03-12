
def i_prime(index):
    if index < 2:
        return False
    for number in range(2, index):
        if index % number == 0:
            return False
    return True


def simple_numbers(info):
    return [i_value for i_index, i_value in enumerate(info) if i_prime(i_index)]


print(simple_numbers('О Дивный Новый мир!'))
#Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']

print(simple_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#Ответ в консоли: [2, 3, 5, 7]