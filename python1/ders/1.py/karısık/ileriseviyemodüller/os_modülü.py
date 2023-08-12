import os
from datetime import datetime

# os.chdir("C:/Users/user/Desktop") change director
# print(os.getcwd())

# for i in os.listdir():
#     print(i)

# os.mkdirs("Deneme2/Deneme2") 
# önce deneme2yi oluşurup sonra onun altına deneme3 ü oluşturuyor

# rmdir remove    removedirs hepsini siler


# print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))


for klasör_yolu,Klasör_isimleri,dosya_isimler in os.walk("C:/Users/ny836/python1"):
    print("Klasör Yolu:",klasör_yolu)
    print("Klasör İsimleri :",Klasör_isimleri)
    print("Dosya İsimleri:",dosya_isimler)
    print("***********************************")






