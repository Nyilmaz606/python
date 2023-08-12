
# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.
"""
 a = int(input("Lütfen bir sayı giriniz:"))
 b = int(input("Lütfen bir sayı giriniz:"))
 c = int(input("Lütfen bir sayı giriniz:"))

 toplam = a * b * c

 print("Birinci Sayı: {} \n İkinci Sayı: {} \n Üçüncü Sayı: {} \n Sayıların Çarpımı: {}".format(a,b,c,toplam))
"""





# Problem 2
# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
boy = float(input("Lütfen boyunuzu giriniz. :"))
kilo = int(input("Lütfen kilonuzu giriniz. :"))

kitle_indeks = kilo / (boy ** 2)

print("Boyunuz: {} \n Kilonuz: {} \n Vücut Kitle Endeksiniz: {} \n".format(boy,kilo,kitle_indeks))

"""





# Problem 3
# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
a = int(input("Aracınız 100 kilometrede ne kadar benzin yakıyor? :"))
b = int(input("Aracınız kaç kilometre yol yaptı? :"))
c = 20.42

bill = b*a*c / 100
 
print("Girdiğiniz Bİlgilere Göre Ödemeniz Gereken Hesap : {} ".format(bill))

"""






# Problem 4
# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""

kullanici_adi = str(input("Lütfen Adınızı Giriniz: "))
kullanici_soyadi = str(input("Lütfen Soyadınızı Giriniz: "))
kullanici_numarasi = int(input("Lütfen Numaranızı Giriniz : "))

print(" {}\n {}\n {} ".format(kullanici_adi,kullanici_soyadi,kullanici_numarasi))


"""




# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

"""
a = int(input("Bir Sayı Girr: "))
b = int(input("Bir Tane Daha Sayı Girr: "))

a, b = b,a


print(" İk girilen değer: {} \n ikinci girilen değer: {} \n Değişme sonrası ilk değer: {}\n Değişme sonrası ikinci değer: {} ".format(a,b,a,b))

"""







# Problem 6
# Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

# Hipotenüs Formülü: a^2 + b^2 = c^2

a = int(input("Dik üçgenin bir kenarını giriniz : "))
b = int(input("Dik üçgenin diğer kenarını giriniz : "))

c = (a**2 + b**2) ** 0.5
# hipotenüs_formulu = a**2 + b**2 = c**2

print("Hipotenüs= {} ".format(c))





















































