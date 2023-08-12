print("**********\nKullanıcı Girişi\n**********\n")


sys_kullaniciadi = "murat"
sys_parola = "12345"
giris_hak = 3
while True :
    kullanıcı_adi = input("Kullanıcı Adı :")
    parola = input("Parola:")
    if (kullanıcı_adi != sys_kullaniciadi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı")
        giris_hak -= 1
    elif (kullanıcı_adi == sys_kullaniciadi and parola != sys_parola):
        print("Kullanıcı Parolası Hatalı")
        giris_hak -= 1
    elif (kullanıcı_adi != sys_kullaniciadi and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı")
        giris_hak -= 1
    else:
        print("Giriş Yapıldı")
        break
    if (giris_hak == 0):
        print("Giriş Hakkıınız Bitti....")
        break