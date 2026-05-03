import random
s = dict()
while len(s) < 10:
    m = random.randint(1, 1000)
    if m not in s:
        a = input(f'Ticket with number {m} giving to: ')
        s[m] = a
    else:
        print(f"Ticket with number {m} is already belongs to {s[m]}, we will take another one.")
for i, j in s.items():
    print(f'Ticket {i} belongs to {j}')