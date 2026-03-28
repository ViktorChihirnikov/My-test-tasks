import os


def read_and_write_file(read_file, write_file):
    # Открываем файлы для чтения и записи
    with open(read_file, 'r', encoding='utf-8') as first_tour, open(write_file, 'w', encoding='utf-8') as second_tour:
        # Список для записи результата
        list_participants = []

        # Выводим имя файла и первую строку из файла
        print('{}\n{}'.format(os.path.basename(path_first_tour), number := int(first_tour.readline())))
        # Циклом, проходим по остальным строкам
        for read_line in first_tour:

            # Выводим содержимое файла
            print(read_line.strip())

            # Строку преобразуем в список и распаковываем результат
            first_name, second_name, score = read_line.split()

            # Условие проверки для записи в словарь
            if int(score) > number:
                list_participants.append([first_name, second_name, int(score)])

        # Записываем в 1-ую строку количество участников
        second_tour.write(str(len(list_participants)) + '\n')

        # Выводим имя файла и первую строку из файла
        print(f'\nСодержимое файла {os.path.basename(path_second_tour)}\n{str(len(list_participants))}')

        # Проходим по отсортированному списку
        for num, write_line in enumerate(sorted(list_participants, key=lambda x: -x[2]), 1):
            # Выводим содержимое файла
            print('{}) {}. {} {}'.format(num, write_line[1][0], write_line[0], write_line[2]))
            # Записываем данные в файл
            second_tour.write('{}) {}. {} {}'.format(num, write_line[1][0], write_line[0], str(write_line[2]) + '\n'))


# Создаём пути к файлам
path_first_tour = os.path.abspath(os.path.join('first_tour.txt'))
path_second_tour = os.path.abspath(os.path.join('second_tour.txt'))
read_and_write_file(path_first_tour, path_second_tour)
