"""
Rewrite the program code below so that it not only displays the asterisks,
but also counts all the asterisks that will be printed when the function is called with an argument of 140. (F(140))

def F( n ):
    print('*')
    if n >= 1:
        print('*')
        F(n-1)
        F(n//2)
"""

def func(n):
    print('*')
    global count
    count += 1
    if n >= 1:
        print('*')
        count += 1
        func(n-1)
        func(n//2)

count = 0
func(140)
print(count)