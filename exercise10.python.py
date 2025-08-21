#DÖVİZ ÇEVİRİCİ(sadece dolar ve euro için)
dolar_oranı=40# 1 dolar 40 tl
euro_oranı=50# 1euro 50 tl
secim=int(input("paranızı dolar yda euro çevirmek istiyorsanız --->1,paranızı tl cevirmek istiyorsanız-->2"))
if secim==1:
    para1=int(input("paranızı girin"))
    cevirme=int(input("dolar için-->3,euro için-->4"))
    if cevirme==3:
        sonuc=para1/dolar_oranı
        print(f"paranız=:{sonuc} dolar")
    else:
        sonuc=para1/euro_oranı
        print(f"paranız=:{sonuc} euro")
else:
    cevirme2=int(input("paranız dolarsa-->5,paranız eurosa-->6"))
         
    para1=int(input("paranızı girin"))
    if cevirme2==5:
        sonuc=para1*dolar_oranı
        print(f"dolardan cevrilmiş paranız=:{sonuc} tl ")
        
    else:
        sonuc=para1*euro_oranı
        print(f"eurodan cevrilmiş paranız=:{sonuc} tl ")





