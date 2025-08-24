#vadeli hesap(kalıtımla)
class hesap:
    def __init__(self,bakiye,para):
        self.para=para
        self.bakiye=bakiye
        
    def goster(self):
         return f"mevcut bakiyeniz:{self.bakiye} "
   
class hesap2(hesap):
    def vadeli_hesap_para_cek(self):
        if self.bakiye<self.para:
         print("bakiyeniz yeterli değil")
        else:
          self.bakiye-=self.para
          return f"mevcut bakiyeniz:{self.bakiye} cekilen  para:{self.para}"
    def vadeli_hesap_para_ekleme(self):
        self.bakiye+=self.para
        return f"mevcut bakiyeniz:{self.bakiye} yatırılan  para:{self.para}"
    
tarih=input("bugunun tarihini gir")
if tarih!="salı":
    print("bu tarihte herhangi bir işlem yapmassınız")
else:
    print("banka mobile hosgeldin para yatırmak istiyorsan -->a,para cekmek istiyorsan -->b,bakiyeyi görmek istiyorsan -->c ye tıklayın lütfen")
    secim=input("secimini girin")
    bakiye=1000
    if secim=="a":

     sayı=int(input("cıkartmka istediğiniz veya eklemek istediğiniz miktarı girin"))
     vadelihesap=hesap2(bakiye,sayı)
     print(vadelihesap.vadeli_hesap_para_ekleme())
    if secim=="b":
         sayı=int(input("cıkartmka istediğiniz veya eklemek istediğiniz miktarı girin"))
         vadelihesap=hesap2(bakiye,sayı)
         print(vadelihesap.vadeli_hesap_para_cek())
    if secim=="c":
        vadelihesap=hesap2(bakiye,0) 
        print(vadelihesap.goster())
        
