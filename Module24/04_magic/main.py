class Water:
    """
    Класс Вода
    """
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm
        elif isinstance(other, Fair):
            return Steam
        elif isinstance(other, Earth):
            return Dirty
        else:
            return None


class Air:
    """
    Класс Воздух
    """

    def __add__(self, other_class):
        if isinstance(other_class, Fair):
            return Lightning
        elif isinstance(other_class, Earth):
            return Dust
        elif isinstance(other_class, Water):
            return Storm
        elif isinstance(other_class, Lightning):
            return Ball_Lightning
        else:
            return None


class Fair:
    """
    Класс Огонь
    """

    def __add__(self, other_class):
        if isinstance(other_class, Earth):
            return Volcano
        elif isinstance(other_class, Water):
            return Steam
        elif isinstance(other_class, Air):
            return Lightning
        else:
            return None


class Earth:
    """
    Класс земля
    """
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirty
        elif isinstance(other, Air):
            return Dust
        elif isinstance(other, Fair):
            return Volcano
        else:
            return None





class Storm:     # Класс Шторм
    answer = 'Шторм шумит кусты трясутся'


class Steam:   # Класс Пар
    answer = 'И ударил горячий пар '


class Dirty: # Класс грязь
    answer = 'И задрожала земля и выплеснула тонну грязи'


class Lightning:   # Класс Молния
    answer = 'Заискрилось небо и разразился гром и УДАРИЛА МОЛНИЯ '

    def __add__(self, other):
        if isinstance(other, Air):
            return Ball_Lightning
        else:
            return None


class Dust: # Класс Пыль
    answer = 'Ого столько пыли я не видел'  # Атрибут класса


class Volcano:  # Лава
    answer = 'И извергнул лава горячая'   # Атрибут класса


class Ball_Lightning:  # Класс Шаровая молния
    answer = 'Ударила гром и спустилась на землю Шаровая молния!!!'  # Атрибут класса





a = Air()        # Создан экземпляр класса Воздух
b = Lightning()  # Создан экземпляр класса Молния
c = a + b         #Сложение Класса Воздух и класса Молния получаем класс Шаровая молния. Это новый класс от сущeствующих по заданию.
print(c.answer)  # Вывод атрибута answer из класса Шаровая молния
