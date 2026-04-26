import random

n = int(input('Введите число: '))
summ, umnoj = 0, 1
for i in range(10):
    x = random.randint(0, n)
    print(x)
    if x % 2 == 0:
        summ += x
    else:
        umnoj *= x
print(summ, umnoj)

