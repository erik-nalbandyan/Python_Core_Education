"""
Using a decorator, print the execution time of the factorial function.
"""

import time

def my_decorator(f):
    def wrapper(n):
        start_time = time.time()
        f(n)
        return f"Function execution time: {time.time() - start_time}"
    return wrapper

@my_decorator
def factorial_counting(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_counting(n-1)

print(factorial_counting(5))