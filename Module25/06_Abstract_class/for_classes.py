from abc import ABC, abstractmethod
import math


class Share(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def area(self):
        print('Забыли переопределить метод!!!')


class Circle(Share):
    """
     Класс для расчёта площади круга Circle
    """

    def __init__(self, radius):
        """
        Конструктор класса
        :param radius: радиус
        :type: int
        """
        self.radius = radius

    def area(self):
        """
        Метод для расчёта площади круга
        :return: int
        """
        return round(math.pi * 5 ** 2, 1)


class Rectangle(Share):
    """
    Класс для расчёта площади прямоугольника Rectangle
    """
    def __init__(self, long, width):
        """
        Конструктор класса Rectangle
        :param long: длина
        :param width: ширина
        :type: int
        """
        self.long = long
        self.width = width

    def area(self):
        """
        Метод для расчёта Прямоугольника
        :return: int
        """
        return 2 * (self.long + self.width)



class Triangle(Share):
    """
    Класс для расчёта Треугольника Triangle
    """

    def __init__(self, base, height):
        """
        Конструктор класса Triangle
        :param base: основание
        :param height: высота
        :type: int
        """
        self.base = base
        self.height = height

    def area(self):
        """
        Метод для расчёта площади треугольника
        :return: int
        """
        return (self.base * self.height) / 2
