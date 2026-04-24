
class MyStack:
    """
    Класс MyStack имеет 2 метода добавление и удаление задачи
    """

    def __init__(self):
        """
        Конструктор класса MyStack
        """
        self.stack = []

    def add_value(self, task: tuple) -> None:
        """
        Метод класса MyStack для добавления стека
        :param task: tuple (int,list)
        :return: None
        """
        self.stack.insert(0, task)

    def del_value(self, task: tuple) -> None:
        """
         Метод класса MyStack для удаления стека
        :param task: tuple (int,list)
        :return: None
        """
        self.stack.remove(task)



class TaskManager:
    """
    Класс TaskManager
    """

    def __init__(self):
        """
        Конструктор класса TaskManager
        :parameter: list  self.task для создания конструктора класса MyStack()
        """
        self.task = MyStack()


    def new_task(self, task, priority):
        """
        Метод класса TaskManager для создания добавления новой задачи в список задач
        :param task: str Название задачи
        :param priority: int номер приоритета задачи
        :return: None
        """
        new_tuple = (priority, [task])
        for nam_task, list_task in self.task.stack:
            if priority == nam_task and task in list_task:
                print('Такая задача уже существует\n')
                break
            elif priority == nam_task and task not in list_task:
                list_task.append(task)
                break
        else:
            self.task.add_value(new_tuple)



    def delite_tasks(self):
        """
        Метод класса TaskManager для удаления задач и отчистки списка
        # - Очистить список
        # - Удалить задачу: Выводит список задач после выбора обращается к методу del_value класса MyStack

        """
        while True:
            try:
                choose = int(input('Очистить весь список - 1, Удалить одну из задач - 2: '))
                if choose == 1:
                    self.task.stack.clear()
                    print(f'Список отчищен {self.task.stack}')
                    return

                elif choose == 2:
                    print(TaskManager.__str__(self))
                    num_task = int(input('Введите номер задачи для удаления: '))
                    for priority in self.task.stack:
                        if num_task == priority[0]:
                            self.task.del_value(priority)
                            return
                    raise IndexError('Введён не существующий номер задачи!!!\n')

                raise IndexError
            except (ValueError, IndexError) as exc:
                print('Ошибка ввода, следуйте указаниям', exc)



    def __str__(self):
        """
        Метод класса TaskManager для вывода результата
        :return: str
        """
        for_add_string = ''
        for priority, task in sorted(self.task.stack, key=lambda x: x[0]):
            for_add_string += f'{priority} - {", ".join(task)}\n'
        return for_add_string



a = TaskManager()
a.new_task('Нужно погулять', 4)
a.new_task('Сделать дела по дому', 5)
a.new_task('Нужно погулять', 4)
a.new_task('Сдать Дз', 2)
a.new_task('I need to buy food', 1)
a.new_task('I need to buy food', 1)
a.new_task('I need to walk', 1)
print(a)
a.delite_tasks()
print(a)
