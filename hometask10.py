# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
from random import randint
amount = int(input('type amount: '))
i = 0 # счетчик
sum0 = 0 # считает решку
sum1 = 0 # считает гербы
while i < amount:
    side = randint(0, 1) # заполняем случайным методом
    # print(side)
    if side == 0:
        sum0 += 1
    else:
        sum1 += 1
    i += 1
# print('=============')
if sum0 < sum1:
    print(sum0)
else:
    print(sum1)
