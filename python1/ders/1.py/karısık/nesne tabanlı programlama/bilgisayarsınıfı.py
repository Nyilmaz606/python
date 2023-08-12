import time
import math
import random
from math import *

class Bilgisayar():

    def __init__(self,model="Monster Abra A7", pcdurum = "Kapalı",işletim_sistemi ="Windows 10 Pro" ,uygulamalar= "VSCode,Google,RDR2"):
        self.model = model
        self.pcdurum = pcdurum
        self.işletim_sistemi = işletim_sistemi
        self.uygulamlar = uygulamalar

    def açma(self):

        if (self.pcdurum == "Açık"):
            print("Pc Zaten Açık.")

        else :
            print("Pc Açılıyor...")
            self.pcdurum = "Açık"

    def kapama(self):

        if (self.pcdurum == "Kapalı"):
            print("Pc Zaten Kapalı.")

        else:
            print("Pc Kapanıyor...")
            time.sleep(1)
            self.pcdurum = "Kapalı"

    def hesap_makinesi(self):

        if (self.pcdurum == "Açık"):

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
        elif (self.pcdurum == "Kapalı"):
            print("Oyuna Başlamak İçin Önce Bilgisayarı Açınız")         

    def sayı_tahmin(self):
        
        if (self.pcdurum == "Açık"):
        
            print("""************************

            Sayı Tahmin Oyunu


            1 ile 40 arasında sayıyı tahmin edin.

            ************************""")


            rastgele_sayı = random.randint(1,40)
            tahmin_hakkı = 0

            while True:
                
                tahmin = int(input("Tahmininiz : "))


                if (tahmin < rastgele_sayı):
                    print("Bilgiler Sorgulanıyor ...")
                    time.sleep(1)
                    print("Daha Yüksek Bir Sayı Tahmin Edin.")
                    
                    tahmin_hakkı+= 1
                elif (tahmin > rastgele_sayı):
                    print("Bilgiler Sorgulanıyor ...")
                    time.sleep(1)
                    print("Daha Düşük Bir Sayı Tahmin Edin.")
                    
                    tahmin_hakkı += 1

                else:
                    print("Bilgiler Sorgulanıyor ...")
                    time.sleep(1)

                    print("Tebrikler Doğru Tahmin Ettiniz. \n Sayı : {} idi".format(rastgele_sayı))
                    tahmin_hakkı += 1
                    print("{}. tahminde doğru bildiniz".format(tahmin_hakkı))
                    break
                
                if (tahmin_hakkı==7):
                    print("Tahmin hakkınız bitmiştir. ")
                    print("Sayımız : {} idi".format(rastgele_sayı))
                    break

        elif (self.pcdurum == "Kapalı"):
            print("Oyuna Başlamak İçin Önce Bilgisayarı Açınız")

    def __str__(self):
        return "Pc Durumu: {}\nModel: {}\nİşletim Sistemi: {}\nUygulamar: {}\n".format(self.pcdurum,self.model,self.işletim_sistemi,self.uygulamlar)
    

    def bilgilerigöster(self):
        if (self.pcdurum == "Açık"):
            print("---------------------------\nBilgisayar Özellikleri\n---------------------------\nModel:{}\nİşletim Sistemi:{}\nPc Durumu:{}\nUygulama Listesi{}\n---------------------------".format(self.model,self.işletim_sistemi,self.pcdurum,self.uygulamlar))



        elif (self.pcdurum == "Kapalı"):
            print("Önce Bilgisayarı Açınız")

bilgisayar = Bilgisayar()

print("""-----------------------------------------
    Bilgisayar İşlemleri
    -----------------------------------------
    1 = AÇMA
    2 = KAPAMA
    3 = HESAP MAKİNESİ
    4 = SAYI TAHMİN OYUNU
    5 = Bilgiler 
    -----------------------------------------""")   

while True:
    cıktı = input("Lütfen Bir İşlem Seçiniz:")


    if cıktı == "Q" or cıktı == "q" :
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        print("Çıkış Yapıldı...")
        time.sleep(1)
        break

    elif cıktı=="1" :
        bilgisayar.açma()

    elif cıktı == "2" :
        bilgisayar.kapama()

    elif cıktı == "3" :
        bilgisayar.hesap_makinesi()

    elif cıktı == "4":
        bilgisayar.sayı_tahmin()

    elif cıktı == "5":
        bilgisayar.bilgilerigöster()

    

    else:
        print("Geçersiz İşlem ")
        time.sleep(1)
        print("Lütfen Tekrardan Bir İşlem Seçiniz")
        time.sleep(1)
        continue