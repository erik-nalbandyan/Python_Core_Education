"""
В файле 17-1.txt содержится последовательность целых чисел.
Элементы последовательности могут принимать целые значения от -10 000 до 10 000 включительно.
Определите количество троек, в которых хотя бы два из трёх элементов меньше,
чем среднее арифметическое всех чисел в файле, и десятичная запись всех трёх элементов тройки содержит цифру 1.
В ответе запишите два числа: сначала количество найденных троек, а затем максимальную сумму элементов таких троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
"""

import random
def main(main_list):
    arithmetic_mean_of_list_all = sum(main_list) // len(main_list)
    counter_of_triple_lists, maximum_summary_of_triple_lists = 0, 0
    for i in range(len(main_list) - 2):
        triple_list = main_list[i:i+3]
        for m in triple_list:
            counter = 0
            if '1' not in str(m):
                break
            for j in triple_list:
                if j < arithmetic_mean_of_list_all:
                    counter += 1
                if counter == 2:
                    counter_of_triple_lists += 1
                    if maximum_summary_of_triple_lists < sum(triple_list):
                        maximum_summary_of_triple_lists = sum(triple_list)
    return counter_of_triple_lists, maximum_summary_of_triple_lists


random_list = [random.randint(-10000, 10001) for i in range(1000)]
print(f"You have {main(random_list)[0]} amount of triples which are required to search "
      f"and here is the max sum of them {main(random_list)[1]}")