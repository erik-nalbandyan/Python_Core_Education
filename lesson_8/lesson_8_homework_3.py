def number_factorial(n):
    if n == 0:
        return f"Factorial of 0 is 1"
    x = 1
    for i in range(1,n+1):
        x *= i
    return f"Factorial of {n} is {x}"


print(number_factorial(3))