print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi
 
3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
""")


a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

islem = input("İşlemi giriniz :")

if islem == "1":
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b) )
elif islem == "2":
    print("{} ile {} in çıkarımı {} dir.".format(a,b,a-b) )
elif islem == "3":
    print("{} ile {} in çarpımı {} dir.".format(a,b,a*b) )
elif islem == "3":   
    print("{} ile {} in bölümü {} dir.".format(a,b,a/b) )

else: 
    print("Geçersiz işlem.")    



    print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi
 
3. Çarpma İşlemi

4. Bölme İşlemi

5. Karesini alma

6. Karekök alma

7. Faktöriyel alma

8. Logaritmasını alma
-----------------------------------------------------------
""")