print("**********\nKullanıcı Girişi\n**********\n")

# Kullanıcı Adı Girişi örneğinin gerçek versiyonunu PyQT5 derslerinde bulabilirsiniz.


sys_kullanıcı_adı = "mmurat"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola :
    print("Parola Hatalı...")
elif kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola :
    print("Kullanıcı Adı Hatalı...")
elif kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola :
    print("Kullanıcı Adı ve Parola Hatalı...")
else :
    print("Sisteme Giriş Yapıldı...")