"""
Элементы последовательности могут принимать целые значения от -10 000 до 10 000 включительно.
Определите количество троек, в которых хотя бы два из трёх элементов меньше,
чем среднее арифметическое всех чисел в файле.
В ответе запишите количество найденных троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
"""

import random
def main(a, func):
    c = 0
    for i in a:
        if func(i):
            c += 1
    return c
random_list = [random.randint(-10000, 10001) for i in range(1000)]
sredni = sum(random_list) / len(random_list)
c = 0
for i in range(len(random_list) - 2):
    triple = random_list[i:i + 3]
    if main(triple, lambda k: k < sredni) >= 2:
        c += 1
print(f"You have {c} amount of triples which are required to search")