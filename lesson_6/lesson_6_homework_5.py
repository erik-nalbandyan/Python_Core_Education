import random
s= []
n = []
m = 0
for i in range(10):
    s += [random.randint(0, 10)]
print(s)
for j in s:
    m += 1
    if j < 5:
        n += [j]
for k in n:
    while s.count(k) > 0:
        s.remove(k)
print(s)
print(sum(s) / len(s))