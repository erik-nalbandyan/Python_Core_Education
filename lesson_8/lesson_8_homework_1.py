import math
s = int(input("Enter circle radius "))
def radius(s):
    circle_area = math.pi * (s ** 2)
    return int(circle_area)


print(radius(s))