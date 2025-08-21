#BASİT ÇEVİRİ UYGULAMASI

ceviri={
"lion":"aslan",
"chair":"sandalye",
"bag":"çanta",
"pillow":"yastık",
"table":"masa",
"blush":"allık",
"scarecrow":"korkuluk",
"towel":"havlu"
}

kelime=input("hangi kelimenin cevirisini görmek istiyorsun lion,chair,bag,pillow,table,blush,scarecrow,towel")
if kelime not in ceviri:
    print("gecersiz kelime")
else:
    print(f" kelime:{ceviri[kelime]} ")

