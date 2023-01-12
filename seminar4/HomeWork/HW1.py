# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal

number = input("Введите число: ")
d = input("Введите требуемую точность в формате '0.001': ")
number = Decimal(number)
number = number.quantize(Decimal(d))
print(number)

