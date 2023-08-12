import random
import time

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