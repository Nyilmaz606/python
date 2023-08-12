from datetime import datetime   
import locale

locale.setlocale(locale.LC_ALL,"")
# şu_an = datetime.now()

# print(datetime.ctime(şu_an))
# print(datetime.strftime(şu_an,"%Y"))
# print(datetime.strftime(şu_an,"%D %B"))
# print(datetime.strftime(şu_an,"%Y %B %A"))




# saniye = datetime.timestamp(şu_an)
# print(saniye)

# şu_an2 = datetime.fromtimestamp(saniye)

# print(şu_an2)




# şu_an = datetime.fromtimestamp(0)
# print(şu_an)


tarih = datetime(2019,12,1)

şu_an = datetime.now()

print(tarih - şu_an)






