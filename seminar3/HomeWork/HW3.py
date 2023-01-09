# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def preobrazovanie_in_binary(number):
    binary_num = ''
    while number > 0:
        binary_num = str(number%2) + binary_num
        number //=2
    return binary_num

num = int(input("Введите десятичное число, которое нужно преобразовать в двоичное :  "))
print(preobrazovanie_in_binary(num))





