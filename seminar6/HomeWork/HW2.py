# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]


result = [i for i in range(20, int(input("Введите значение n: ")) + 1) if i % 20 == 0 or i % 21 == 0]
print(result)

