from collections.abc import Iterable


def generator(num: int) -> Iterable[int]:
    """
    Функция генератор -> number ** 2
    :param num: int
    :return: Iterable[int]
    """
    for number in range(1, num + 1):
        yield number ** 2


for element in generator(10):
    print(element)
