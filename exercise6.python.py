liste=["meyve","bal","süt","un","seker"]

print(" hangi işaretleri kullanmak istiyorsun 1>ekle,2-->cıkar,3-->listele")
isaret=int(input("işaretinin temsil ettiği sayıyı gir"))
if isaret==1:
    sayı=int(input("kac tane sey eklemek istiyorsun"))
    for i in range(sayı):
        eklenen_sey=input("eklemek istediklerinizi sırasıyla girin")
        liste.append(eklenen_sey)
elif isaret==2:
    sayı2=int(input("kac tane ürün cıkarmak istiyorsun"))
    for i in range(sayı2):
        cıkarılan_sey=input("hangi ürünü veya ürünleri çıkarmak istiyorsunuz sırasıyla girin")
        try:
            liste.remove(cıkarılan_sey)
        except ValueError:
            print(f"{cıkarılan_sey} listede yok!")

elif isaret==3:
    for i in range(1,len(liste)+1):
        print(f"{i},")


 