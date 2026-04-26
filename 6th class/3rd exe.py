s = []
for i in range(10):
    s += [int(input('Enter a number:'))]
print(s)
del s[2::2]
print(s)