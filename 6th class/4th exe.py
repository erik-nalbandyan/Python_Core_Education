import random
s = []
for i in range(10):
    s += [random.randint(0,100)]
s1 = sorted(s)
print(s1)
print(s1[1] + s1[-2])