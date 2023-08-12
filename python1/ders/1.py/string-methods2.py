website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Proglamlama Rehberiniz (40 saat)"

# 1 Hello World karekter dizisinin baş ve sondaki boşluk karakterlerini silin

result = " Hello World ".strip()
result = " Hello World ".lstrip()
result = " Hello World ".rstrip()

result = website.lstrip("//:htp")

result = "nurettin.yılmaz".strip("zam")

result = website.count("a")
result = website.count("www")
result = website.count("www", 0,10)

result = website.startswith("www")
result = website.startswith("http")
result = website.endswith("com")


result = website.find("com")
result = course.find("com", 0,11)

result = website.index("com")
# result = website.rindex("com")  ^# exception hata demek

result = course.isalpha()
result = "Hello".isalpha()
result = course.isdigit()
result = "126546".isdigit()

result = "Contents".center(80, "*")
result = "Contents".ljust(80 , "*")
result = "Contents".rjust(15,"o")

result = course.replace(" ", "-",5)
result = course.replace(" ", "",)

result = "Hello World".replace("World" ,"There")

result = course.split(" ")
# result = result[7]





print(result)