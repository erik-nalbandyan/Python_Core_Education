"""
Write a program that counts the number of lines in the attached file.
The file must be located in the same directory as the program.

P.S. Do not include lines that represent gaps (empty lines) between parts of the poem in the count.

zadanie2.txt
"""

with open("zadanie2.txt") as fl:
    print(len(list(filter(lambda x: x != '\n', fl.readlines()))))