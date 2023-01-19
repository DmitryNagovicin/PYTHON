# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

str = 'абв'
count = int(input("Введите количество слов в списке: "))
if count < 0:
    print("The data is incorrect")
our_list = ' '.join(''.join(random.sample(str, 3)) for i in range(count))

result = [i for i in our_list.split() if str not in i]

print(our_list)
print(' '.join(result))
