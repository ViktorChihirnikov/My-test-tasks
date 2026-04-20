import random


class Parents:

    def __init__(self, name, age):
        """
        Конструктор класса Parents.
        :param name: str Имя родителя
        :param age: int Возраст родителя
        """
        self.name = name
        self.age = int(age)
        self.list_children = []

    def put_children(self, name, age):
        """
        Метод класса Parents. Проверяет, и создаёт объект класса Child
        :param name: Str ИМя ребёнка
        :param age: int Возраст ребёнка
        :return: None
        """
        if self.age - int(age) >= 18:
            self.list_children.append(Child(name, age))
        else:
            print('Возраст родителя не соответствует условию')

    def do_spoken_shut(self):
        """
        Метод класса Parents. Проверяет состояние ребёнка и выводит сообщении.
        :return: None
        """
        print('Нужно проверить ребёнка!!!!\n')
        for child in self.list_children:
            result = child.spoken_child()
            if result == 1:
                print('Дам ему игрушку\n')
            elif result == 2:
                print('Не буду мешать\n')
            elif result == 3:
                print('Пойду успокою\n')
            elif result == 5:
                print('Пойду покормлю\n')
            else:
                print('Что то тихо, пойду проверю\n')

    def __str__(self):
        """
        Метод класса Parents
        :return: str Информацию о родителе
        """
        return 'Имя родителя: {}\nВозраст: {}\nДети: {}.\n'.format(self.name.title(), self.age,
                                                                   ", ".join(ch.name for ch in self.list_children))


class Child:
    spoken = {1: 'Ребёнок играет', 2: 'Ребёнок спит', 3: 'Ребёнок плачет', 4: 'Ребёнок молчит', 5: 'Ребёнок голоден'}

    def __init__(self, name, age):
        """
        Конструктор класса Child
        :param name: str Имя ребёнка
        :param age: int Возраст рёбёнка
        """
        self.name = name
        self.age = int(age)

    def spoken_child(self):
        """
        Метод класса Child. Метод выводит Имя ребёнка и возвращает рандомный результат.
        Выбор происходит из списка ключей
        :return: int
        """
        result_spoken = random.choice(list(self.spoken.keys()))
        print(f'Имя: {self.name}. {self.spoken[result_spoken]}')
        return result_spoken


# Создадим Родителя
parents = Parents('Мария', '36')
# Добавим детей
parents.put_children('Вася', 1)
parents.put_children('Маша', 3)
# Выведем информацию
print(parents)
parents.do_spoken_shut()
