f = int(input('Введите число '))
n = 1
m = 1
if f > 0:
    while n <= f:
        print(n, end=' | ')
        m *= n
        n += 1
    print('Факториал вашего числа равно ', m)
elif f < 0:
    print('Это отрицательное число')