"""
Write a function that takes two parameters: a filename and an opening mode
(the filename is entered by the user, while the mode is specified as a literal when the function is called).
The function should count the number of words in the given file and return that count.
You can use the text file from Task 2 for testing.
"""


def word_counting_function(n, type_of_operation):
    with open(n, type_of_operation, encoding='utf-8') as fl:
        s = fl.read().split()
        return len(s)

name_of_file = input("Enter file name: ")
print(word_counting_function(name_of_file, input('Enter type of operation ')))
