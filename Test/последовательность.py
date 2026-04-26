n = int(input('Введите количество чисел в последовательности: '))
summ = 0
for x in range(n):
    m = int(input('Введите число: '))
    if m % 6 == 0:
        summ += m
print('Сумма чисел кратных 6-и равно: ', summ)
