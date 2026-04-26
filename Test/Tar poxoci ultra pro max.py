pox = input("Напишите что-нибудь по братски)): ")
simbol = input("А теперь напиши тоже что нибудь по братски, только это чтобы символ был а по братски((: ")
while len(simbol) > 1:
    print("Эу не мороси!!!")
    simbol = input("Давай по новой: ")
print("Вот те на лови аптечку:", pox.replace('a', simbol.lower()).replace('A', simbol.upper()))