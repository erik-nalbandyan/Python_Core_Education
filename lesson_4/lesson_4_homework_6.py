N = int(input('Введите число: '))
if N > 0:
    for i in range(1, N + 1):
        if i % 2 != 0:
            print(i, 'в степени 3 = ', i ** 3)
        else:
            print(i, 'в степени 2 = ', i ** 2)
elif N == 0:
    print('Нафига мне твой 0?')
else:
    print('Вы ввели отрицательное число(')