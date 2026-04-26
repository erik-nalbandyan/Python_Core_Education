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
for i in slovar.keys():
    if len(i) <= 4:
        print(i)
for i in slovar.values():
    if len(i) >= 5:
        print(i)