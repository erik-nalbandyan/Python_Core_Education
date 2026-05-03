import random
s, l = [], 1
for i in range(20):
    s += [random.randint(0, 20)]
print(s)
n = s[2::2]
print(n)
for i in n:
    if i % 3 == 0:
        l *= i
print(l)