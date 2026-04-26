m = "AGDBBEFAAFHFDBFDDHHHBDFFBCCHHF"
s = []
k = 'F4'
for i in m:
    if i == 'A':
        k = k.replace(k[0], chr(ord(k[0]) - 1))
        k = k.replace(k[1], str(int(k[1]) + 2))
        s.append(k)
    elif i == "B":
        k = k.replace(k[0], chr(ord(k[0]) + 1))
        k= k.replace(k[1], str(int(k[1]) + 2))
        s.append(k)
    elif i == "C":
        k = k.replace(k[0], chr(ord(k[0]) + 2))
        k = k.replace(k[1], str(int(k[1]) + 1))
        s.append(k)
    elif i == "D":
        k = k.replace(k[0], chr(ord(k[0]) + 2))
        k = k.replace(k[1], str(int(k[1]) - 1))
        s.append(k)
    elif i == "E":
        k = k.replace(k[0], chr(ord(k[0]) + 1))
        k = k.replace(k[1], str(int(k[1]) - 2))
        s.append(k)
    elif i == "F":
        k = k.replace(k[0], chr(ord(k[0]) - 1))
        k = k.replace(k[1], str(int(k[1]) - 2))
        s.append(k)
    elif i == "G":
        k = k.replace(k[0], chr(ord(k[0]) - 2))
        k = k.replace(k[1], str(int(k[1]) - 1))
        s.append(k)
    elif i == "H":
        k = k.replace(k[0], chr(ord(k[0]) - 2))
        k = k.replace(k[1], str(int(k[1]) + 1))
        s.append(k)
print(s)