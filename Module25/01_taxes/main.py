
class Property:
    tax = 0
    """
    Родительский класс Property
       Args:
           self.__worth: принимает значение int через метод с проверкой ввода
           tax: принимает int и в наследуемом классе меняется для расчёта

    """
    def __init__(self, worth):
        """
        Конструктор класса Property
        :param worth: принимает str и передаётся в сеттер
        """
        self.__worth = self.check_worth(worth)


    def __str__(self):
        """
        Метод для вывода значения расчёта налога
        :return: str
        """
        return f'Расчёт налога 1/{self.tax}'


    def check_worth(self, arg):
        """
         Метод для контроля ввода и изменения закрытого аргумента.
        :parameter arg: Принимает int
        :return int
        """
        while arg <= 0:
            print('Стоимость должна быть больше нуля!!')
            arg = int(input('Введите стоимость:'))
        return arg


    def calculate_taxes(self, money):
        """
        Метод для расчёта налога
        :return: int
        """
        percent = self.__worth / self.tax
        print('Сумма налога -', percent, 'руб')
        if money - percent < 0:
            print('Сумма которой нехватает -', money - percent, 'руб')


class Apartment(Property):
    tax = 1000
    """
    Класс Apartment от родительского класса Property
    Arguments:
             tax: int значение для расчёта налога
        
    """
    def __init__(self, arg):
        """
        Конструктор класса Apartment
        :param arg: принимает str и передаётся в сеттере в родительский конструктор классов.
        """
        super().__init__(arg)


class Car(Property):
    tax = 200
    """
     Класс Car от родительского класса Property
     Arguments:
              tax: int значение для расчёта налога

    """

    def __init__(self, arg):
        """
        Конструктор класса Apartment
        :param arg: принимает str и передаётся в сеттере через родительский конструктор классов
        """
        super().__init__(arg)


class House(Property):
    tax = 500
    """
        Класс House от родительского класса Property
        Arguments:
                 tax: int значение для расчёта налога
    """

    def __init__(self, arg):
        """
         Конструктор класса House
         :param arg: принимает str и передаётся в сеттере через родительский конструктор классов
        """
        super().__init__(arg)



while True:
    try:
        print('\n1- Налог на квартиру, 2- Налог на машину, 3- Налог на Дом: ', end='')
        choice = int(input())
        if choice < 4:
            cost = int(input('Введите стоимость: '))
            have_money = int(input('Введите наличие денег: '))

            if choice == 1:
                apartment = Apartment(cost)
                apartment.calculate_taxes(have_money)
            elif choice == 2:
                car = Car(cost)
                car.calculate_taxes(have_money)

            elif choice == 3:
                house = House(cost)
                house.calculate_taxes(have_money)

    except ValueError as exc:
        print('Ошибка ввода проверьте правильность ввода и следуйте рекомендациям!!!', exc)
