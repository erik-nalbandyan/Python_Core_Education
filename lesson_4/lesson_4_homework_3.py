while True:
    T = int(input('Введите число больше 34: '))
    if T >= 35:
        for i in range(1, T):
            if i == 7 or i == 13 or i == 21 or i == 29:
                continue
            print(i)
        break
    else:
        print('Число не соответствует требованию')