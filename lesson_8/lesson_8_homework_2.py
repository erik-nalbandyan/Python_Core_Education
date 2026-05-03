def even_digit_counter(number):
    sum, counter= 0, 0
    n = number
    while n > 0:
        x = n % 10
        if x % 2 == 0:
            sum += x
            counter += 1
        n //= 10
    return f'Number {number} has {counter} even digits and here is their summary: {sum}'


print(even_digit_counter(245))