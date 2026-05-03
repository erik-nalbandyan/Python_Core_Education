"""
Break the given file into 4 separate files, with one paragraph per file.

zadanie3.txt
"""

with open("zadanie3.txt", encoding='utf-8') as fl:
    s = fl.read().split('\n\n')
    c = 0
    for i in s:
        c += 1
        with open(f'obzac_{c}.txt', 'w', encoding='utf-8') as f:
            print(i, file=f, end='')
