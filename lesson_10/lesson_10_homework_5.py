"""
Write a function that takes a filename as input.
The function should return the following information about the file:

Number of lines (sentences)
Number of words
Number of integers
Number of punctuation marks (periods, commas, question marks, etc.)

Use one of the attached text files for testing.

zadanie5-us.txt
zadanie5.txt
"""

import string

def my_func(name_of_file):
    with open(name_of_file, encoding='utf-8') as f:
        file = f.read()
        new_list_for_counting_digits = []
        number_of_sentences = len(file.split('.'))
        number_of_words = len(file.split())
        for j in file.split():
            for char in string.punctuation:
                while char in j:
                    j = j.replace(char, "")
            new_list_for_counting_digits.append(j)
        number_of_digits = len(list(filter(lambda x: x.isdigit(), new_list_for_counting_digits)))
        number_of_punctuation = 0
        for i in file:
            if i in string.punctuation:
                number_of_punctuation += 1

    return print(f"""Current file: {name_of_file}

Number of sentences: {number_of_sentences}
Number of words: {number_of_words}
Number of digits: {number_of_digits}
Number of punctuation: {number_of_punctuation}""")


my_func("zadanie5.txt")
