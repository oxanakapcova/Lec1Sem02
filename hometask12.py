# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
from math import sqrt

s = int(input('type sum: '))
p = int(input('type multiplication: '))
# x + y = s
# x * y = p
# y = s - x
# x * (s-x) = p -> x*s - x**2 - p = 0 -> x**2 - x*s + p = 0
# решаем квадратное уравнение с дискриминантом, дискриминант положительный значит
# корней может быть 2
# d = b**2 - 4*a*c = 25 -24=1
# x1 = (-s + sqrt(d)) / 2*a
# x2 = (-s - sqrt(d)) / 2 * a
# y1 = s - x1; y2 = s - y2
d = s**2 - 4 * p # дополнительная переменная дискриминанта
x1 = int((s + sqrt(d)) / 2)
y1 = s - x1
print(f'first solution: x = {x1}, y = {y1}')
x2 = int((s - sqrt(d)) / 2)
y2 = s - x2
print(f'second solution: x = {x2}, y = {y2}')
# можно убрать вывод второго решения, он меняет местами корни


