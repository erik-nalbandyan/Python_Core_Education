n = int(input('Введите целое число '))
summ = 0
m = 0
if n > 0 or n < 0:
    while n > 0:
        x = n % 10
        if x % 2 == 0:
            summ += x
            m += 1
        n //= 10
else:
    print('Почему именно 0 а?')
print('Количество чётных цифр в вашем цифре равно ', m)
print('Сумма чётных цифр равно ', summ)


