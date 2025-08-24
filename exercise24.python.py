import random
class sayıTahminOyunu:
    def __init__(self,alt=1,ust=100):
        self.alt=alt
        self.ust=ust
        self.sayı=random.randint(alt,ust)
        self.deneme=0
    def tahmin_et(self,tahmin):
        self.deneme+=1
        if tahmin<self.sayı:
            return "daha buyuk bir sayı gir"
        elif tahmin >self.sayı:
            return "daha buyuk bir sayı gir"
        else:
            return f"teprikler! {self.deneme} denemde buldun"
oyun=SayıTahminOyunu()
while True:
    tahmin=int(input("tahmini girin:"))
    sonuc=oyun.tahmin_et(tahmin)
    print(sonuc)
    if"teprikler" in sonuc:
        break