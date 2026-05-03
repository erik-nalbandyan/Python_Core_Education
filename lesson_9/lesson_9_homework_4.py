"""
A 10-element list filled with random numbers from 1 to 20.
Based on this list, create a new list in which the even elements of the first list
are multiplied by 2 and the odd elements by 3.
Use the map() and lambda functions.
Print the original list and the resulting list.
"""


import random

s = [random.randint(1,21) for i in range(10)]
print(s)
print(list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, s)))