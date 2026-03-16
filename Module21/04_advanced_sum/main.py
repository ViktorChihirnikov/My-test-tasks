def new_sum(element, index=0):
    value = element[index % len(element)]
    summ = 0
    if index == len(element):
        return summ
    elif isinstance(value, int):
        summ += value
    elif isinstance(value, list):
        summ += new_sum(value)
    summ += new_sum(element, index + 1)
    return summ



a = [[1, 2, [3]], [1], 3]
#a = [1, 2, [3], 4]
#Ответ в консоли: 10

b = (1, 2, 3, 4, 5)
#Ответ в консоли: 15

result = new_sum(a)

print(result)