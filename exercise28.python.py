#Müşteri sınıfı (birden fazla hesap)
class musteri:
    def __init__(self,ad,soyadı,):
       self.ad=ad
       self.soyadı=soyadı
       self.hesap_liste=[]
    def hesap_ekle(self,hesap):
        self.hesap_liste.append(hesap)
    def hesap_goster(self):
        for i, hesap in enumerate(self.hesap_liste, start=1):
            print(f"{i}. Hesap -> {hesap.goster()}")
class Hesap:
    def __init__(self, bakiye):
        self.bakiye = bakiye

    def goster(self):
        return f"Mevcut bakiyeniz: {self.bakiye}"

m1=musteri("ali","çetin")
secim=input("a-->hesap goster,  b--->hesap ekle")
if secim=="a":
  m1.hesap_goster()
elif secim=="b":
    bakiye = int(input("Yeni hesap için bakiye gir: "))
    yeni_hesap = Hesap(bakiye)
    m1.hesap_ekle(yeni_hesap)
    print("yeni hesap eklendi")
    m1.hesap_goster()



        
        