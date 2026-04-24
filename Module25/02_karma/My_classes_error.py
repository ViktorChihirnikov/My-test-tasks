
class KillError(Exception):
    """
    Созданный класс KillError от базового класса Exception
    """
    def __str__(self):
        return f'Ошибки не убивают а делают сильней'


class DrunkError(Exception):
    """
    Созданный класс DrunkError от базового класса Exception
    """
    def __str__(self):
        return f'Пьянству бой'


class CarCrashError(Exception):
    """
    Созданный класс CarCrashError от базового класса Exception
    """

    def __str__(self):
        return f'Так бывает'


class GluttonyError(Exception):

    """
    Созданный класс GluttonyError от базового класса Exception
    """
    def __str__(self):
        return f'Заедаем'


class DepressionError(Exception):
    """
    Созданный класс DepressionError от базового класса Exception
    """
    def __str__(self):
        return f'Опять что то пошло не так'

