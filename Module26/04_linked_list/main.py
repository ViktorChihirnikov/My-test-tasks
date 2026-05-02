from typing import Optional, Any, Iterable, Iterator


class Node:
    """
    Класс Node, для создания узлов связного списка.
    """

    def __init__(self, value=None, next_value=None) -> None:
        """
        Конструктор класса Node, для создания узла в связном списке.
        :param value: Optional[Any] (параметр принимает любое значение)
        :param next_value:  (параметр принимает ссылку, на следующие значение в новом узле)
        """
        self.num = value
        self.next_num = next_value




class Linkedlist:
    """
    Класс Linkedlist для создания связного списка
    """

    def __init__(self) -> None:
        """
        Конструктор класс Linkedlist
        :param: head (Принимает первый узел связного списка и является головой этого списка)
        """
        self.head = None




    def append(self, add_value: Optional[Any]) -> None:
        """
        Метод append, класса Linkedlist принимает 1 любой аргумент. Создаёт узел и передаёт ссылку на следующий узел
        :param add_value: Optional[Any]
        :return: None
        """
        # Создаём новый узел, обращаясь к классу Node и передаем принимаемый аргумент методом.
        new_node = Node(add_value)

        # Условие с проверкой для создания головного узла, связного списка
        if self.head is None:
            self.head = new_node
            return

        # Если проверка не сработала, значит головной узел есть и следует итерироваться по списку
        # для нахождения узла, где параметр для ссылки на следующий узел будет None.
        last_node = self.head
        while last_node.next_num:
            last_node = last_node.next_num
        last_node.next_num = new_node




    def get(self, index_value_of_list: int) -> Optional[Any]:
        """
        Метод get класса Linkedlist для нахождения значения по индексу.
        :param index_value_of_list:
        :return:
        """
        # Так как связной список индексов не имеет, то объявляется счётчик и итератор, с условием
        # Счетчик увеличивается на 1, при проходе одного узла.
        index = 0
        head_current = self.head
        while head_current is not None:
            if index == index_value_of_list:
                return head_current.num
            head_current = head_current.next_num
            index += 1
        else:
            raise LookupError('Не корректный индекс для вывода значения')




    def pop(self, index_value_of_list: int) -> Optional[Any]:
        """
        Метод pop() класса Linkedlist, для удаления узла из списка по индексу.
        :param index_value_of_list: Int
        :return: None
        """
        # Текущий узел
        head_current = self.head

        # Инициализируем переменную для индекса
        index = 0

        # Проверка совпадения по индексу.
        if index == index_value_of_list:

            # Проверка дает возможность, исключить что голова не имеет ссылку на следующий узел.
            # И если ссылка есть то ссылка на следующий узел становится головой. А проверяемый узел удаляется.
            # Если ссылки на следующий узел нет, то проверяемый узел является единственным в списке, то есть голова.
            # То его удаляем и выходим Удаление происходит через присваивание к self.head = None.
            if head_current.next_num is not None:
                self.head = head_current.next_num
                return
            self.head = None
            return

        # Инициализируем переменную last_node для сохранения головы, если предыдущие, условие не сработало.
        last_node = head_current

        # Перезаписываем в head_current следующую ссылку так как первый узел не подходит для удаления и далее проверка
        #   будет произведена с последующего узла в списке, Index увеличен на 1.
        head_current, index = head_current.next_num, 1

        # Цикл с условием, начинается со второго элемента в списке
        while head_current is not None:

            # Проверка сравнения по индексу
            if index == index_value_of_list:

                # Проверка дает возможность, исключить что узел не имеет ссылку на следующий узел и удаление
                if head_current.next_num is not None:
                    last_node.next_num = head_current.next_num
                    break
                last_node.next_num = None
                break
            last_node = head_current
            head_current = head_current.next_num
            index += 1
        # Если цикл отработал и не найдено по индексу значение для удаления, то выбрасывается ошибка.
        else:
            raise LookupError('Не корректный индекс для удаления')



    def __iter__(self) -> Iterator:
        """
        Метод iter класса Linkedlist
        :return: Iterator
        """
        return self



    def __next__(self) -> Iterable[Any]:
        """
        Метод next класса Linkedlist
        :return: Iterable[Any]
        """
        # Условие для выхода.
        if self.head is not None:

            # Берем значение из текущего узла.
            data_current = self.head.num

            # Изменяем голову на следующий узел
            self.head = self.head.next_num

            # Возвращаем текущее значение.
            return data_current

        raise StopIteration



    def __str__(self) -> str:
        """
        Метод str класса Linkedlist
        :return: str
        """
        head_current = self.head
        list_str = ''
        while head_current is not None:
            if head_current.next_num is None:
                list_str += str(head_current.num) + ''
            else:
                list_str += str(head_current.num) + ' '
            head_current = head_current.next_num
        return f'[{list_str}]'


try:
    # Создаём объект класса Linkedlist и через метод класса append() добавляем значения.
    my_list = Linkedlist()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(50)

    # Удаления значения по индексу.
    my_list.pop(1)

    # Получения значения по индексу.
    print(my_list.get(0))

    # Итерация объекта
    for value in my_list:
        print(value, end=' ')

    # Выводит весь список
    #print(my_list)

except (LookupError, StopIteration) as error:
    print(error)

else:
    print(my_list)



