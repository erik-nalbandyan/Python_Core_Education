slovar = {
    "кот" : 'cat',
    "собака" : 'dog',
    "медведь" : 'bear',
    "ластик" : 'eraser',
    "ложка" : 'spoon',
    "взгляд" : 'sight',
    "раковина" : 'sink',
    "наушники" : 'earphones',
    "пляж" : 'beach',
    "дорога" : 'road'
}
for i in range(5):
    a = input('please enter russian word: ')
    b = input('Enter translation in english: ')
    slovar[a] = b
print(slovar)