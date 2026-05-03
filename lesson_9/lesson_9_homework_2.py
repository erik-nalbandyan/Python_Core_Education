"""
Using recursion, write a function that prints Fibonacci numbers.
The function takes as an argument the number of elements in the sequence, starting with 0.
A Fibonacci number is a sequence in which the next number is equal to the sum of the two preceding numbers.
"""

def fibonacci(n):
    if n <= 1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Enter a number: '))
for i in range(n):
    print(fibonacci(i))
