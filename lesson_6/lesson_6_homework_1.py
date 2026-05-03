text = list(input("Enter some text pls: "))
while text.count("a") > 0:
    text.remove("a")
while text.count("e") > 0:
    text.remove("e")
while text.count("u") > 0:
    text.remove("u")
print(text)

