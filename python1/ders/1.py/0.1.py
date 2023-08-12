"""
    Daire Alanı : 
    Daire Çevresi :     

    Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız 
    (pi:3.14)

"""

pi = (3.14)
r = float(input("YarıCap: "))

daireAlanı = (pi * (r ** 2))
daireCevresi = 2*pi*r


print("daireAlanı: " + str(daireAlanı))
print("daireCevresi: " + str(daireCevresi))

