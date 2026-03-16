import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def new_sait(info_dict, **kwargs):
    for key, value in kwargs.items():
        if key in info_dict:
            info_dict[key] = value
            return info_dict
        for key_info_dict in info_dict.values():
            if isinstance(key_info_dict, dict):
                new_sait(key_info_dict, **kwargs)
    return info_dict


def make_sait(passed_site):
    quantity = int(input('Сколько сделать сайтов? '))
    sait_list = []
    for _ in range(quantity):
        name_the_thing = input('Введите название продукта: ').title()
        copy_site = copy.deepcopy(passed_site)
        changed_site = new_sait(copy_site, title=f'Куплю/продам телефон {name_the_thing} недорого',
                                h2=f'У нас самые лучшие условия на {name_the_thing}')
        sait_list.append(changed_site)
    return sait_list


result_list_site = make_sait(site)
print(f'Список ваших сайтов \n{result_list_site}')


