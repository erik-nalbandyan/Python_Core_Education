import random
x = random.randint(0, 4)

while True:
    n = int(input('Попробуйте угадать число от 0 до 4: '))
    if 0 <= n <= 4:
        if n == x:
            print('Поздравляю вы угадали число ;)')
            break
        else:
            print('Неправильно ;(')
    else:
        print('Число не соответствует требованию')