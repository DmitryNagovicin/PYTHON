# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, 
# содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'],
#  'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def diction(*name):
    name_list = [*name]
    dictionary = {}
    for name in name_list:
        name.capitalize()
        capital = name[0]
        if capital in dictionary.keys():
            dictionary[capital].append(name)
        else: 
            dict_1 = [name]
            dictionary[capital] = dict_1
    return dictionary


print(diction("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
