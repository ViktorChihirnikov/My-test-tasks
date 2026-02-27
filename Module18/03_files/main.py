name_file = input('Введите название файла: ')
simbols = tuple('@№$%^&\*()')
simbols_end = ('.txt', '.docx')

if name_file.startswith(simbols):
    print('Ошибка, название начинается на один из специальных символов')

elif not name_file.endswith(simbols_end):
    print('Не правильное расширение! правильное .txt или .docx')

else:
    print('Файл назван верно')
