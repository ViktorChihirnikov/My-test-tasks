students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}



def sorted_info(info_dict):
    id_ages = []
    hobby = set()
    long = 0
    for i_id in info_dict:
        id_ages.append((i_id, info_dict[i_id]['age']))
        hobby.update(set(info_dict[i_id]['interests']))
        long += len(info_dict[i_id].get('surname'))
    return id_ages, hobby, long


id_and_ages, interesting, long_surnames = sorted_info(students)
print(f'ID-возраст:{id_and_ages}\nИнтересы:{interesting}\nСумма длины всех фамилий:{long_surnames}')
