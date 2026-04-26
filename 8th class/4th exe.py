import  random
def sorted_list_of_even_numbers(*args):
    x = []
    print(args)
    for i in args:
        if i % 2 == 0:
            x.append(i)
    return sorted(list(set(x)), reverse=True)

print(sorted_list_of_even_numbers(*[random.randint(1, 30) for i in range(15)]))
