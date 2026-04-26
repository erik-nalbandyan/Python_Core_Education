import random
mn, bn = set(), set()
while len(mn) < 20:
    mn.add(random.randint(1,100))
while len(bn) < 20:
    bn.add(random.randint(1,100))
print(mn,bn,mn|bn,mn&bn,mn-bn,sep="\n")
