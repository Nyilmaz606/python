def tambolenleribulma(sayı):
    tam_boolenler = []

    for i in range(2,sayı):

        if (sayı % i == 0):
            tam_boolenler.append(i)
    return tam_boolenler


while True:
    sayı = input("Sayı Girin : ")

    if (sayı == "q"):
        break

    else:
        sayı = int(sayı)

        print(tambolenleribulma(sayı))
