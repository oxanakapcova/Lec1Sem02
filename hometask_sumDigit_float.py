# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр. Пример:
# - 6782 -> 23
# - 0,56 -> 11

s = input('Type number: ')
digit_sum = 0
for i in range(len(s)):
    if s[i].isdigit():
        digit_sum += int(s[i])
print(digit_sum)

