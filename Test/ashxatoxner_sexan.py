try:
    number_of_employes = int(input('Сколко рабочих в одном кабинете? '))
    if number_of_employes < 0:
        print('Нельзя вводить отрицательное значение для сотрудников, они же люди ;(')
    elif number_of_employes == 0:
        print(1)
    else:
        print((number_of_employes - 1) // 2 + (number_of_employes - 1) % 2 + 2)
except ZeroDivisionError:
    print('zroi chbajanvav')
except Exception:
    print('chelav')
