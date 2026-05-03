import random
def sorted_set(*args):
    return list(set(args))


print(sorted_set(*[random.randint(1, 10) for i in range(20)]))