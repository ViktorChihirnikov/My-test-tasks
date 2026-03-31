import math


def get_sage_sqrt(value):
    try:
        if isinstance(value, (str, dict, tuple, list)):
            raise TypeError('Тип данных должен быть float или int')
        elif value < 0:
            raise ValueError('Число не может быть отрицательным')
    except (ValueError, TypeError) as exc:
        return exc
    except BaseException as exc:
        return f'Не предвиденная ошибка{exc}'
    else:
        return math.sqrt(value)



numbers = [16, 25, -9, 0, 4.5, "abc", {1: 2}]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень {number}: {result}")
