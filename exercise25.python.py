import random
class oyun:
    secenekler=["taş","kağıt","makas"]
    def __init__(self,oyuncu_adı):
        self.oyuncu_adı=oyuncu_adı
    def bilgisiyar(self):
        return random.choice(self.secenekler)
    def karsılastır(self,oyuncu,bilgisiyar):
        if oyuncu==bilgisiyar:
            return "berabere!"
        elif(oyuncu=="taş" and bilgisiyar=="makas" )or\
             (oyuncu=="kağıt" and bilgisiyar=="taş") or\
             (oyuncu=="makas" and bilgisiyar=="kağıt"):
             return f"{self.oyuncu_adı} kazandı!"
        else:
            return "biligisiyar kazandı"
oyun=oyun("oyuncu1")
while True:
    oyuncu_hamle=input("taş,maka veyakağıt gir çıkış için q")
    if oyuncu_hamle=="q":
        break
    if oyuncu_hamle not in oyun.secenekler:
        print("geçersiz seçim yaptınız")
        continue
    bilgisiyar=oyun.bilgisiyar()
    print(f"bilgisiyar:{bilgisiyar}")
    print(oyun.karsılastır(oyuncu_hamle,bilgisiyar))
    


