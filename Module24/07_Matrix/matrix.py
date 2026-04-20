class Matrix:
    """
    Класс Matrix содержит методы сложение, вычитание, умножение, транспортировку матрицы Данный класс используется как
    модуль
    """

    def __init__(self, count: int, size: int) -> None:
        """
        Конструктор класса Matrix создаёт матрицу по принимаемым аргументам
        :param count: int количество значений во вложенном списке
        :param size: int количество вложенных списков
        """
        self.data = [[num for num in range(count, count + size)] for count in range(1, count * size + 1, size)]
        self.data_transpose = [[num for num in range(size, size + count)] for size in range(1, size * count + 1, count)]


    def __add__(self, other: list) -> str:
        """
        Магический метод класса Matrix принимает другой список/матрицу и складывает с текущей матрицей
        :param other: list
        :return: str
        """
        result = [[i + j for i, j in zip(current, out_data)]for current, out_data in zip(self.data, other)]
        return self.make_string(result)

    def __sub__(self, other: list) -> str:
        """
        Магический метод класса Matrix принимает другой список/матрицу и вычитает из текущей матрицей
        :param other: list
        :return: str
        """
        result = [[i - j for i, j in zip(current, out_data)] for current, out_data in zip(self.data, other)]
        return self.make_string(result)

    def __mul__(self, other: list) -> str:
        """
        Магический метод класса Matrix принимает другой список/матрицу и умножает с текущей матрицей
        :param other: list
        :return: str
        """
        new_data = []
        result_1 = 0
        result_2 = 0
        for current_data in self.data:
            for current_value, mul in zip(current_data, other):
                result_1 += current_value * mul[0]
                result_2 += current_value * mul[1]
            new_data.append([result_1, result_2])
            result_1 = 0
            result_2 = 0
        return self.make_string(new_data)

    def __str__(self):
        """
        Магический метод класса Matrix выводит текущую матрицу
        :return: str
        """
        return self.make_string(self.data)


    def make_string(self, data: list[list[int]]) -> str:
        """
        Метод класса Matrix принимает аргумент типа list[int] создаёт строки из аргументов списка и возвращает
        :param data: list[int]
        :return: str
        """
        string = ''
        for i_list in data:
            for value in i_list:
                string += str(value) + '   ' + '\t'
            string += '\n'
        return string


    def transpose(self) -> str:
        """
        Метод класса Matrix транспортирует матрицу из строки делает столбцы
        :return: str
        """
        for index, list_data in enumerate(self.data):
            for value_of_list, list_transpose in zip(list_data, self.data_transpose):
                value_of_list, list_transpose[index] = list_transpose[index], value_of_list
        return self.make_string(self.data_transpose)

