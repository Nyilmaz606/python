print("""*****************
Atm'ye hoşgeldiniz.

İşlemler;
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Çıkış yapmak için q'ya basınız..
*****************""")

bakiye = 1000

while True:
    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("İşlem Sonlandırıldı.")
        break
    
    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))
    
    elif (işlem == "2"):   
        miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz: ")) 
        bakiye += miktar
        print("Para Yatırma İşlemi Tamamlandı Yeni Bakiye {}".format(bakiye))
    
    elif (işlem == "3"):
        miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz: ")) 
        if (bakiye - miktar < 0 ):
            print("Böyle Bir Miktar Çekemezsiniz.")
            continue
        bakiye -= miktar
        print("Para Çekme İşlemi Tamamlandı Yeni Bakiye {}".format(bakiye))

    else :
        print("Hatalı İşlem")