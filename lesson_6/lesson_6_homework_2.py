import random
n = int(input("Enter a number of numbers in list pls: "))
s = []
for i in range(n):
    s += [random.randint(0,20)]
print(s)