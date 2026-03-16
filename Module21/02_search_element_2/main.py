site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(info_dict, element, level_count=0, step_info=0):
    if element in info_dict and step_info == level_count:
        return info_dict.get(element)
    for value in info_dict.values():
        if isinstance(value, dict):
            result = search(value, element, level_count, step_info + 1)
            if result:
                return result

    else:
        return None



info_key = input('Введите искомый ключ: ')
depth = input('Хотите ввести максимальную глубину? Y/N: ').upper()
if depth == 'N':
    result_search = search(site, info_key)
    if result_search:
        print(f'Значение ключа {info_key}: {result_search}')
    else:
        print('Ключ не найден!')
else:
    count = int(input('Введите глубину 0т 1 до 2: '))
    result_search = search(site, info_key, count)
    if result_search:
        print(f'Значение ключа {info_key}: {result_search}')
    else:
        print('Ключ не найден, проверьте правильность ввода глубину или введите правильный ключ!')

