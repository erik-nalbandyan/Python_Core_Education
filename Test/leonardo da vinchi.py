a = 23
b = 42
sum = 0
for i in range(28):
    sum = a + b
    if sum % 2 == 0:
        sum -= 1
    a, b = b, sum
    print(sum, i)
