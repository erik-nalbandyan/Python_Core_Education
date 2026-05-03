text = input("Qez asum em gri ay txa eeeeeeee:")
sum = ''
for i in text.swapcase().split():
    sum += i
print(sum)