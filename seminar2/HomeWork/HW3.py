# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num = int(input("Введите число: "))
sum_list = 0
list_num = []
for i in range (num):
    i += 1
    list_num.append((1 + 1/i)**i)
    sum_list += ((1 + 1/i)**i)
print(list_num)
print(sum_list)