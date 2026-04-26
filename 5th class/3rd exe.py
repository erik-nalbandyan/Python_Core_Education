text = input('Текст пиши а внатуре уже нервируешь:')
sum = 0
for i in text:
    if i.isdigit():
        sum += 1
if sum > 0:
    print(f"В введенной строке : {sum} цифр")
else:
    print("В данном предложении нету цифр")