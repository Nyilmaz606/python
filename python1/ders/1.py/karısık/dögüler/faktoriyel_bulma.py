print("""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************""")

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Çıkış Yapıldı...")
        break

    else:
        sayı = int(sayı)
        faktoriyel = 1
    for i in range(2,sayı+1):
        faktoriyel *= i
    print("Faktoriyel: {} ".format(faktoriyel))