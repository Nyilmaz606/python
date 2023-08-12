9
# Problem 1
# Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

#  Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

#  BKİ 18.5'un altındaysa -------> Zayıf

#  BKİ 18.5 ile 25 arasındaysa ------> Normal

#  BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

#  BKİ 30'un üstündeyse -------------> Obez

"""

kilo = float(input("Lütfen Kilonuzu Giriniz: "))
boy = float(input("Lütfen Boyunuzu Giriniz: "))

indeks = kilo / (boy * boy)

if indeks < 18.5 :
    print("Zayıf")

elif 25 > indeks > 18.5 :
    print("Normal")

elif 25 < indeks < 30 : 
    print("Fazla Kilolu")

else:
    print("Obez")

print(indeks)

"""



# Problem 2
# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

"""
a = int(input("Lütfen bir sayı giriniz: "))
b = int(input("Lütfen bir sayı giriniz: "))
c = int(input("Lütfen bir sayı giriniz: "))

if a > b and a > c :
    print(a)

elif b > a and b > c :
    print(b)

elif a == b == c :
    print("Girdiğiniz bütün sayılar eşit.")
    print(a)
else:
    print(c)

"""








# Problem 3
# Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

#     Vize1 toplam notun %30'una etki edecek.

#     Vize2 toplam notun %30'una etki edecek.

#     Final toplam notun %40'ına etki edecek.


#     Toplam Not >=  90 -----> AA

#     Toplam Not >=  85 -----> BA

#     Toplam Not >=  80 -----> BB

#     Toplam Not >=  75 -----> CB

#     Toplam Not >=  70 -----> CC

#     Toplam Not >=  65 -----> DC

#     Toplam Not >=  60 -----> DD

#     Toplam Not >=  55 -----> FD

#     Toplam Not <  55 -----> FF


"""
vize1 = float(input("1. vizeden aldığınız notu girin :"))
vize2 = float(input("2. vizeden aldığınız notu girin :"))
final=float(input("Finalden aldığınız notu girin :"))

ort = float(vize1 * 30/100  + vize2 * 30 / 100 + final * 40 / 100 )

print(ort)


if ort >= 90 : 
    print("Notunuz AA")

elif ort >= 85 : 
    print("Notunuz BA")

elif ort >= 80 : 
    print("Notunuz BB")

elif ort >= 75 : 
    print("Notunuz CB")

elif ort >= 70 : 
    print("Notunuz CC")

elif ort >= 65 : 
    print("Notunuz DC")

elif ort >= 60 : 
    print("Notunuz DD")

elif ort >= 55 : 
    print("Notunuz FD")

elif ort >= 50 : 
    print("Notunuz FF")

else :
    print("Kaldın....")

"""










# Problem 4
# Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

# Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

# Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
#  Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

# Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.


print("Kullanabileceğiniz Geometrik Şekiller \n Üçgen \n Dörtgen")

a = (input)("Kullanmak istediğiniz geometrik şekli yazınız : ")

if a == "Üçgen" :
    k =(input)("Lütfen bir kenarı giriniz: ")
    l = (input)("Lütfen bir kenarı giriniz: ")
    m = (input)("Lütfen bir kenarı giriniz: ")
    
    if k == l : 
        print("Bu İkizkenar bir üçgendir.")
    elif k == m :
        print("Bu İkizkenar bir üçgendir.")
    elif l == m :
        print("Bu İkizkenar bir üçgendir.")
    elif k == l == m :
        print("Bu Eşkenar bir üçgendir.")
    elif k != l and l != m and m != k :
        print("Bu çeşitkenar bir üçgendir.")
    else : 
        print("Bir Üçgen Belirtmiyor")    



elif a == "Dörtgen":
    z = (input)("Lütfen bir kenarı giriniz: ")
    x = (input)("Lütfen bir kenarı giriniz: ")
    y = (input)("Lütfen bir kenarı giriniz: ")
    v = (input)("Lütfen bir kenarı giriniz: ")

    if z == x and y == v:
        print("Bu bir Dikdörtgendir.")

    elif z == y and x == v : 
        print("Bu bir Dikdörtgendir.")
    
    elif z == v and y == x :
        print("Bu bir Dikdörtgendir.")

    elif z == y == x == v :
       print("Bu bir Karedir.") 

    else :
        print("Bu bir Dörtgendir.")