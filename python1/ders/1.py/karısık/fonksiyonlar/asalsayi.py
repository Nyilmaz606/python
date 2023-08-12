


def asalsayi(sayı):
    if(sayı == 0):
        return False

    elif (sayı == 2):
        return True

    else :
        for i in range(2,sayı):
            if (sayı % i == 0 ):
                return False
            return True

while True:
    sayı = input("Sayı Gir : ")
    if (sayı == "q"):
        break

    else:
        sayı = int(sayı)
        if (asalsayi(sayı)):
            print(sayı,"Sayı Asaldır.")
        else:
            print(sayı,"Sayı Asal Değil.")
