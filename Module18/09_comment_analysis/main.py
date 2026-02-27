def count_uppercase_lowercase(text):
    count = [0, 0]
    for i in text:
        if i.isupper():
            count[0] += 1
        elif i.islower():
            count[1] += 1
    return count


# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
