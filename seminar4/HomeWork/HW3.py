# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random

rand_list = []
n = int(input("Введите количество элементов списка: "))
for i in range(n):
    rand_list.append(random.randint(1, 10))
print(rand_list)

final_list = []
for i in rand_list:
    if rand_list.count(i) == 1:
        final_list += [i]
print(final_list)
