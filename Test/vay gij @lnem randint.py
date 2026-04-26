import random

s = [random.randint(1,100) for i in range(100)]
ax = 1
for i in range(0, len(s), 2):
    if s[i] > 20 and s[i] < 100:
        ax *= s[i]
print(ax)