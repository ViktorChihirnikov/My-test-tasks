class Student:

    def __init__(self, args):
        """
        Конструктор класса Student содержит Имя, фамилию, номер группы, оценку
        :param args:
        """
        self.first_name = args[0]
        self.last_name = args[1]
        self.number_class = int(args[2])
        self.progress = int(args[3])

    def __str__(self):
        """
        Метод класса Student, для вывода информации
        :return: str
        """
        return f'{self.first_name}, {self.last_name}, {self.number_class}, {self.progress}'


class MakeInfoStudent:

    def __init__(self, count_data):
        """
        Конструктор класса MakeInfoStudent
        :param count_data: Int Колл-во создаваемых карточек
        """
        self.list_students = []
        self.count_data = count_data
        self.input_info_about_student()
        self.sort_data()

    def input_info_about_student(self):
        """
        Метод класса MakeInfoStudent. Запрашивает у пользователя данные студента и создаёт объект класса
        Student и добавляет в список.
        :return: None
        """
        while len(self.list_students) < self.count_data:
            info_student = input('Введите через пробел!!! Имя, фамилию, номер группы, успеваемость: ').title().split()

            if (len(info_student) == 4 and info_student[0].isalpha() and info_student[1].isalpha()
                    and info_student[2].isnumeric() and info_student[3].isnumeric()):
                self.list_students.append(Student(info_student))
            else:
                print('Проверьте данные, Имя фамилия это буквы, далее цифры', " ".join(info_student))


    def sort_data(self):
        """
        Метод сортировки и вывода списка
        :return: None
        """
        for student in sorted(self.list_students, key=lambda x: x.progress):
            print(student)



MakeInfoStudent(3)
