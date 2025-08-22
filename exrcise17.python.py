import random
print("zar oyununa hosgeldin")
print("ilk yirmiye ulaşan kazanır iyi şansalar")
oyuncu_puan=0
oyuncu_puan2=0
while oyuncu_puan<=20 and oyuncu_puan2<=20 :
    print("oyuncu 1 zar atmak için entere bas")
    zar1=random.randint(1,6)
    oyuncu_puan+=zar1
    print(f"1. oyuncu puanı:{oyuncu_puan}")
    if oyuncu_puan==20:
        print("teprikler kazandın")
        break
    print("oyuncu 2 zar atmak için entere bas")
    zar2=random.randint(1,6)
    oyuncu_puan2+=zar2
    print(f" 2. oyuncu puanı:{oyuncu_puan2}")
    if oyuncu_puan2==20:
        print("teprikler kazandın")
        break
    