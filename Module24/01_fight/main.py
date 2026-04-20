import random


class Unit:
    """
    Класс Unit
    """
    health = 100

    def __init__(self, name):
        """
        Конструктор класса Unit
        :param name: Имя бойца: str
        """
        self. name = name


    def get_damage(self, name_is_doing_hit):
        """
        Функция для расчёта здоровья
        :param name_is_doing_hit: Имя бойца который нанёс удар: str
        :return: bool
        """
        self.health -= 20
        self.info(name_is_doing_hit)
        return self.health



    def info(self, name_is_doing_hit):
        """
        Функция для вывода информации
        :param name_is_doing_hit: Имя бойца нанёсший урон: str
        :return str
        """
        print('Ударил {}\nУ {} осталось здоровья {}\n'.
              format(name_is_doing_hit, self.name, self.health))



class GameControl:
    """
    Класс GameControl
    """

    def __init__(self, list_1):
        """
        Конструктор класса GameControl, Генерация списка экземпляров класса Unit
        :param list_1: Имина бойцов
        """
        self.name_list = [Unit(name) for name in list_1]
        self.fight()

    def fight(self):
        """
        Метод класса, рандомно выберет бойца, который ударит. И по индексу возьмёт бойца который получает урон
        :return: None
        """
        result = True
        while result:
            give_hit = random.choice(self.name_list)
            get_hit = self.name_list[(self.name_list.index(give_hit) + 1) % len(self.name_list)]
            result = get_hit.get_damage(give_hit.name)
        print(f'Победил {give_hit.name}')



list_name = ['Тайсон', 'Мухамед Али']
GameControl(list_name)












