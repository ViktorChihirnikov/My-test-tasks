import random


class Person:
    """
    Класс Person.
    Содержит атрибуты на уровне класса
    """
    satiety = 50
    house = True

    def __init__(self, name):
        """
        Конструктор класса Person
        :param name: str
        """
        self.name = name

    def eat(self):
        """
        Метод класса, выводит сообщение, что нужно поесть и увеличивает параметр сытости
        :return: None
        """
        print(self.name, 'Нужно поесть')
        self.satiety += 1


    def work(self):
        """
         Метод класса, выводит сообщение, что нужно поработать и уменьшает параметр сытости
        :return:
        """
        print(self.name.title(), 'Нужно поработать')
        self.satiety -= 1


    def play(self):
        """
        Метод класса, выводит сообщение, что есть время покататься на велосипеде -
        и уменьшает параметр сытости.
        :return:
        """
        print(self.name, 'Отлично, есть время покататься на велосипеде')
        self.satiety -= 1


    def go_to_a_shop_food(self):
        """
        Метод класса выводит сообщение о том что нужно пойти на работу
        :return:
        """
        print(self.name, 'Пойду в магазин за едой')


class House:
    fridge = 50
    table_for_money = 0

    def __init__(self, list_name):
        """
        Конструктор класса House
        :param list_name:
        """
        self.list_name = [Person(i_name) for i_name in list_name]


    def live(self, count):
        """
        Метод класса.
        1. Выводит текущий день, параметр еда и денег
        2. Рандомно выбирает число
        3. В цикле, берёт объект класса Person и согласно условию работает с объектом класса Pеrson
        :param count: int Параметр принимает число, это номер дня.
        :return: None
        """
        print(f'\nДень:{count}')
        print(f'Еда:{self.fridge}\nДенег:{self.table_for_money}')
        for do in self.list_name:
            kube = random.randint(1, 6)
            if do.satiety < 10:
                do.eat()
                self.fridge -= 1
            elif self.fridge < 10:
                do.go_to_a_shop_food()
                self.fridge += 1
                self.table_for_money -= 1
            elif self.table_for_money < 50 or kube == 1:
                do.work()
                self.table_for_money += 1
            elif kube == 1:
                do.work()
                self.fridge -= 1
            elif kube == 2:
                do.eat()
            else:
                do.play()


# Создадим объект класса House и передадим туда список с аргументами
live_in_the_house = House(['Муж', 'Жена'])
# В цикле вызываем метод класса House и передаём туда аргумент/номер дня
for i in range(366):
    live_in_the_house.live(i)

