class Mydict(dict):
    """
    Класс Mydict от производного класса dict
    """

    def get(self, key):
        """
        Изменённый метод класса Mydict от родителя dict
          изменёно возвращаемое значение с None на 0.
        :param key: принимает int or str
        :return: Если ключ присутствует в словаре то value иначе 0
        """
        return super().get(key, 0)



b = {'q': 1, 'w': 2, 'e': 3}
a = Mydict(b)
print(a.get('u'))