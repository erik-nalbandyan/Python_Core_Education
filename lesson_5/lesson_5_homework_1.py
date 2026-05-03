text = input("Введите 2 слова:")
sum = ''
while len(text.split()) != 2:
    text = input("Вы ввели что-то неправильно, попробуйте снова:")
sum += text.split()[1] + ' ' + text.split()[0]
print(sum)