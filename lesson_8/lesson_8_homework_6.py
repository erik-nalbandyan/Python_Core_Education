def playpipi(s):
    print(f'Our number is {s}')
    for i in range(2, s):
        if s % i == 0:
            print(f"Number {s} is prime number")
            break
        elif i - s == -1:
            print(f"Number {s} is composite numbers")
    def inner(s):
        if s %  3 == 0:
            print(f"Number {s} is devided by 3")
        else:
            print(f"Number {s} is not devided by 3")
    inner(s)
    return "Thats just it :0"

print(playpipi(int(input("Pls input a number in the end "))))