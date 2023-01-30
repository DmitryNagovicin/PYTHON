# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

import random

rand_list = []

n = int(input("Введите количество элементов списка: "))
for i in range(n):
    rand_list.append(random.randint(1, 30))
print(rand_list)

final_list = [rand_list[i] for i in range(1, len(rand_list)) if rand_list[i] > rand_list[i - 1]]
print(final_list)
