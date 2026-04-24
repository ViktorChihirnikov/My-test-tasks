from My_classes_error import CarCrashError, KillError, DrunkError, DepressionError, GluttonyError
import random


class Buddha:
    """
    Класс Buddha
    :argument: MAX_KARMA int
    """

    def __init__(self):
        self.__MAX_KARMA = 500


    def get_max_karma(self):
        """
        Геттер
        :return: int
        """
        return self.__MAX_KARMA


    def set_karma(self, arg_max_karma):
        """
        Сеттер принимает аргумент и осуществляет контроль ввода на int.
           :param arg_max_karma: Принимает int.
           :return int
        """
        while arg_max_karma.isalpha():
            arg_max_karma = input('Введите значение кармы: ')
        self.__MAX_KARMA = int(arg_max_karma)

    def one_day(self):
        """
        Метод класса Buddha
        Properties:
              result: рандомно число int  or str если выбирается 'error' то выбрасывает raise
              :raise: выбрасывает ошибку KillError, DrunkError, CarCrashError, GluttonyError, DepressionError
                      от родителя класса Exception
        :return: int рандомно число

        """
        result = random.choice([1, 2, 3, 4, 5, 6, 7, 0, 0, 'error'])
        if result == 'error':
            choice_error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            raise choice_error
        return result


person = Buddha()
karma = 0
with open('karma.log', 'w', encoding='utf-8') as write_error:
    while person.get_max_karma() >= karma:
        try:
            karma += person.one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            write_error.write(str(exc) + '\n')
