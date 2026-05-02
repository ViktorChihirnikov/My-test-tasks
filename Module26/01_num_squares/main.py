
class MyIterator:
    count = 0
    """
    Класс итератор, возвращает квадрат числа
    :parameter: count: int
    
    """

    def __init__(self, number: int) -> None:
        """
        Конструктор класса MyIterator
        :param number: int
        """
        self._number = number



    def __iter__(self):
        """
        Метод iter
        :return: self ссылку на итератор
        """
        self.count = 0  # если в методе указаны параметры класса то итератор можно использовать не 1 раз.
        return self

    def __next__(self) -> int:
        """
        Метод next класса MyIterator
        :return: int
        """
        if self.count < self._number:
            self.count += 1
            return self.count ** 2
        raise StopIteration


result = MyIterator(10)
# 1-й запуск
for num in result:
    print(num)
# 2-й запуск показывает что можно использовать его не 1-раз
for num_1 in result:
    print(num_1)
