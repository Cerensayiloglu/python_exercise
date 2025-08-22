import random
sayı2=[1,2,3,4,5,6,7,8,9,]
sayı2=[1,2,3,4,5,6,7,8,9,10,11,12]
islem=["+","-"]
a=random.choice(sayı1)
op=random.choice(islem)
b=random.choice(sayı2)
print("hosgeldiniz burada toplama ve cıkarma egzersizleri yapabilirsiniz")
print(f"{a} {op} {c} =?")
sonuc=int(input("sonucu nedir"))
if op=="+":
   toplam=a+b
   if sonuc==toplam:
       print("teprikler doğru bildin")
   else:
       print(f"yanlıs tahmin ettin dogru cevap:{toplam}")

if op=="-":
     cıkarım=a+b
     if sonuc==cıkarım:
       print("teprikler doğru bildin")
     else:
       print(f"yanlıs tahmin ettin dogru cevap:{cıkarım}")