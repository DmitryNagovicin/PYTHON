# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8


from random import sample


def fill_list(count):
    if count < 0:
        print("Введите значение больше 0!")
        
    list_nums = sample(range(1, (count + 1) * 2), k=count)
    return list_nums



def find_sum(list_nums):
    sum_list = 0
    for i in range(0, len(list_nums), 2):
        sum_list += list_nums[i]
    print("Сумма элементов списка, стоящих на нечётных позициях : " + str(sum_list))



our_list = fill_list(int(input("Введите количество элементов списка : ")))
print(our_list)
find_sum(our_list)
