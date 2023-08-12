
from math import *
import time

print("\n **************************************** \n Hesap Makinesi Programına Hoş Geldiniz \n ****************************************")
time.sleep(0.7)
print("1. Toplama İşlemi")
time.sleep(0.7)
print("2. Çıkarma İşlemi")
time.sleep(0.7)
print("3. Çarpma İşlemi")
time.sleep(0.7)
print("4. Bölme İşlemi")
time.sleep(0.7)
print("5. Karesini Alma")
time.sleep(0.7)
print("6. Karekök Alma")
time.sleep(0.7)
print("7. Faktöriyel Alma")
time.sleep(0.7)
print("8. Logaritmasını Alma")
time.sleep(0.7)


while True:
    islem = input("İşelmi Seçiniz : ")
    if islem == ("q") or islem == ("Q"):
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        print("Çıkış Yapıldı.")
        break
    elif islem == ("1"):
        print("İşlem Seçiliyor...")
        time.sleep(1)
        toplama1 = int(input("İlk Sayıyı Giriniz : "))
        toplama2 = int(input("İkinci Sayıyı Giriniz : "))

        print("{} ile {} toplamı {} ' dır.".format(toplama1,toplama2,toplama1+toplama2))

    elif islem == ("2"):
        print("İşlem Seçiliyor...")
        time.sleep(1)
        cıkarma1 = int(input("İlk Sayıyı Giriniz : "))
        cıkarma2 = int(input("İkinci Sayıyı Giriniz : "))

        print("{} den {} çıkan {} ' dır.".format(cıkarma1,cıkarma2,cıkarma1-cıkarma2))

    elif islem == ("3"):
        print("İşlem Seçiliyor...")
        time.sleep(1)   
        carpma1 = int(input("İlk Sayıyı Giriniz : "))
        carpma2 = int(input("İkinci Sayıyı Giriniz : "))
        print("{} ile {} nin çarpımı {} ' dır.".format(carpma1,carpma2,carpma1*carpma2))

   
    elif islem == ("4"):
        print("İşlem Seçiliyor...")
        time.sleep(1)   
        bolme1 = int(input("İlk Sayıyı Giriniz : "))
        bolme2 = int(input("İkinci Sayıyı Giriniz : "))
        print("{} ile {} nin bölümü {} ' dır.".format(bolme1,bolme2,bolme1/bolme2))


    elif islem == ("5"):
        print("İşlem Seçiliyor...")
        time.sleep(1)   
        kuvvet1 = int(input("Kuvvetini Almak İstediğiniz Sayıyı Giriniz : "))
        kuvvet2 = int(input("Üssünü  Almak İstediğiniz Sayıyı Giriniz : "))
        print("{} üzeri {} = {}".format(kuvvet1,kuvvet2,pow(kuvvet1,kuvvet2)))
    
        
    elif islem == ("6") :
        print("İşlem Seçiliyor...")
        time.sleep(1)
        karekok1 = int(input("Karekökünü Bulmak İstediğiniz Sayıyı Giriniz : "))
        print("{} in karekökü {}'dir ".format(karekok1,sqrt(karekok1)))

    
    elif islem == ("7") :
        print("İşlem Seçiliyor...")
        time.sleep(1)
        fak = int(input("Faktöriyelini Bulmak İstediğiniz Sayıyı Giriniz : "))
        print("{} in faktöriyeli {}'dir ".format(fak,factorial(fak)))

    elif islem == ("8") :
        print("İşlem Seçiliyor...")
        time.sleep(1)
        log = int(input("Logaritmasını Bulmak İstediğiniz Sayıyı Giriniz : "))
        print("{} in Logaritması {}'dir ".format(log,log10(log)))

    else:
        print("Hatalı Bir İşlem Girdiniz.")
        time.sleep(1)
        print("Tekrardan Bir İşlem Seçiniz.")
        time.sleep(1)
        continue
        

   

