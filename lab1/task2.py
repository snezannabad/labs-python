# TODO Найдите количество книг, которое можно разместить на дискете
dis = 1.44*1024**2
pages = 100
str = 50
symv = 25
viv = int(dis//(str*symv*pages*4))
print("Количество книг, помещающихся на дискету:", viv)
