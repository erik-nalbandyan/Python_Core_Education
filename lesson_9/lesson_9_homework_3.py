"""
Using a lambda expression and the filter function, create a program that, from an input string,
creates a list containing only numeric characters.
"""


def digit_maker_pro_max(digit_argument):
    list_of_only_digits = list(filter(lambda x: x.isdigit(), digit_argument))
    return list_of_only_digits


s = input("Enter a string: ")
print(digit_maker_pro_max(s))
