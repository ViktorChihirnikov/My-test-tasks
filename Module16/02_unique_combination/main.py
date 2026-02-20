def delite_copy_num(a, b):
    a.extend(b)
    c = a.copy()
    for i in c:
        while a.count(i) > 1:
            a.remove(i)
    return a


list1 = [2, 4, 3, 3, 3, 4, 7, 0, 1]
list2 = [2, 4, 5, 6, 8, 10]
merge = delite_copy_num(list1, list2)
merge.sort()
print(f'С применением sort: {merge}')
print(f'С применением sorted: {sorted(merge)}')

print(f'\n****************** Пример-2 ******************')
lists1 = [2, 4, 3, 3, 3, 4, 7, 0, 1]
lists2 = [2, 4, 5, 6, 8, 10]
merge = set(lists1) | set(lists2)
print(f'С применением set {list(merge)}')
