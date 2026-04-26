telephone = {
    'Mike' : {
        'phone' : '094384858',
        'email' : 'makabuyc@mail.ru',
    },
    'Valod' : {
        'phone' : '07719464',
        'email' : 'jrimard@yahoo.com',
    }
}
for i in telephone.keys():
    print(f"{i} имеет следущие данные: ")
    for j, m in telephone[i].items():
        print(j, m)