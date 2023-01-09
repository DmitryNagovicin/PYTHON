# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


from random import sample


def fill_list(count):
    if count < 0:
        print("Введите значение больше 0!")

    list_nums = sample(range(1, count * 2), count)
    return list_nums



def proizv_par(list_nums):
    len_list = len(list_nums)

    for i in range(len_list // 2):
        print(list_nums[i] * list_nums[len_list - i - 1])

    if len_list % 2:
        print(list_nums[len_list // 2])
    


our_list = fill_list(int(input("Введите количество элементов списка: ")))
print(our_list)
print(proizv_par(our_list))