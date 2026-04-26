number = int(input("Input a number: "))
summ = 1
n = 0
while number > 0:
    a = number % 10
    if a % 2 == 0:
        summ *= a
        n += 1
    number //= 10
print('The sum is', summ)
print('The quantity of numbers =', n)