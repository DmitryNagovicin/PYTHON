# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

print("Введите номер четверти")
num = int(input())
if num == 1:
    print("В 1 четверти возможны x > 0 и y > 0")
if num == 2:
    print("В 2 четверти возможны x < 0 и y > 0")
if num == 3:
    print("В 3 четверти возможны x < 0 и y < 0")
if num == 4:
    print("В 4 четверти возможны x > 0 и y < 0")
if num not in range(1, 5):
    print("Нет такой четверти")
