import time

def decor(func):
    def wrapper(a):
        start_time = time.time()
        func(a)
        print(f"Function execution time {time.time() - start_time}")
    return wrapper

@decor
def my_func(a):
    my_list = sorted([i for i in range(2, a ** 2) if i % 2 == 0])
    print(my_list)
    def inner1():
        print("Running 1st inner function")
        list_num1 = []
        for i in my_list:
            if i % 8 == 0:
                list_num1.append(i)
        print(f"Here is a list of nums which are deviable by 8: {list_num1}")
    def inner2():
        print("Running 2nd inner function")
        list_num2 = []
        for i in my_list:
            if i % 6 == 0:
                list_num2.append(i)
        print(f"Here is a list of nums which are deviable by 6: {list_num2}")
    if a % 2 == 0:
        return inner1()
    else:
        return inner2()

my_func(int(input("Enter a number: ")))