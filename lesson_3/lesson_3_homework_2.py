month = int(input("Введите ваш месяц рождения: "))
if month == 12 or  1 <= month <= 2:
    print('Вы родились зимой')
elif  3 <= month <= 5:
    print('Вы родились весной')
elif  6 <= month <= 8:
    print('Вы родились летом')
elif  9 <= month <= 11:
    print('Вы родились осенью')
else:
    print('Нет такого месяца(')